from flask import request, render_template, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app
from .user_model import User

from .user_controller import create_user, get_all_json_users, verify


@app.route('/user', methods=['GET', 'POST'])
def user_root():
    if request.method == 'GET':
        return get_all_json_users()
    elif request.method == 'POST':
        username = request.get_json()['username']
        email = request.get_json()['email']
        if username and email:
            new_user = create_user(username, email)
            return make_response(f"{new_user} successfully created!")
        return make_response(f"failed to create user.. email {email} username {username}")


@app.route('/user/verify-credentials' methods=['GET']
def user_verify_credentials():
    username = request.args.username
    password = request.args.password
