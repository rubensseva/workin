from flask import request, render_template, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app
from workin_api.user.user_model import User

from workin_api.user.user_controller import create_user, get_all_json_users, login_user, verify_jwt

def require_auth(func):
    def wrapper():
        print("Something is happening before the function is called.")
        print(request.headers.get('Authorization'))
        unverified_token = request.headers.get('Authorization').split(' ')[1]
        print(unverified_token)
        print(request.get_json())
        try:
            decoded_jwt_obj = verify_jwt(unverified_token)
            print('got token', decoded_jwt_obj)
            return func()
        except:
            print('login failed!')
            return failed_login()
        print("Something is happening after the function is called.")
    return wrapper

def failed_login():
    return jsonify({'status': 'Token was not valid, login failed'})

@app.route('/user', methods=['GET', 'POST'])
@require_auth
def user_root():
    if request.method == 'GET':
        return get_all_json_users()
    elif request.method == 'POST':
        username = request.get_json()['username']
        email = request.get_json()['email']
        password = request.get_json()['password']
        if username and email and password:
            new_user = create_user(username, email, password)
            return jsonify({'status': f'{new_user} successfully created!'})
        return jsonify({'status': f"failed to create user.. email {email} username {username}"})


@app.route('/user/login', methods=['POST'])
def user_login():
    username = request.get_json()['username']
    password = request.get_json()['password']
    new_jwt = login_user(username, password)
    print(new_jwt)
    if not new_jwt:
        print('login failed...')
        return make_response('Authentication failed...')
    return jsonify({
        'status': 'Authentication success',
        'auth_token': new_jwt
        })



