import sys
from flask import request, render_template, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app
from workin_api.user.user_model import User
from workin_api.shared.auth_helpers import require_auth

from workin_api.user.user_controller import create_user, get_all_json_users, login_user, verify_jwt


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
            try:
                new_user = create_user(username, email, password)
                return jsonify({'status': 'Success', 'msg': f'{new_user} successfully created!'})
            except Exception as e:
                print('Error occured', str(e))
                return jsonify({'status': 'Failed', 'msg': 'Error occured when attempting to create user', 'err': str(e)})
        return jsonify({'status': 'Failed', 'msg': f"failed to create user, some required params not set. Request obj: {request.get_json()}"})


@app.route('/user/login', methods=['POST'])
def user_login():
    username = request.get_json()['username']
    password = request.get_json()['password']
    new_jwt = login_user(username, password)
    print(new_jwt)
    if not new_jwt:
        print('login failed...')
        return jsonify({'status': 'Failed', 'msg': 'Authentication failed, username or password not correct'})
    return jsonify({
        'status': 'Success',
        'msg': 'Authentication success',
        'auth_token': new_jwt
        })



