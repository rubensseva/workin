from flask import request, render_template, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app
from workin_api.user.user_model import User

from workin_api.user.user_controller import create_user, get_all_json_users, verify_user_password


@app.route('/user', methods=['GET', 'POST'])
def user_root():
    if request.method == 'GET':
        return get_all_json_users()
    elif request.method == 'POST':
        username = request.get_json()['username']
        email = request.get_json()['email']
        password = request.get_json()['password']
        if username and email and password:
            new_user = create_user(username, email, password)
            return make_response(f"{new_user} successfully created!")
        return make_response(f"failed to create user.. email {email} username {username}")


@app.route('/user/verify-credentials', methods=['GET'])
def user_verify_credentials():
    username = request.args.get('username')
    password = request.args.get('password')
    isVerified = verify_user_password(username, password)
    if isVerified:
        return make_response('Authentication success!')
    return make_response('Authentication failed...')
