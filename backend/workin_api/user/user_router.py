from flask import request, jsonify

from flask import current_app as app
from workin_api.shared.auth_controller import authorize
from workin_api.shared.exceptions import TokenAuthError, ResourceNotFoundError
from workin_api.shared.utils import create_response, create_login_success_response, Status
from workin_api.user.user_controller import create_user, get_all_json_users, get_personal_data, login_user


@app.route('/user', methods=['GET'])
def user_get():
    try:
        token = authorize()
        if 'user_id' in request.args:
            return get_personal_data(
                int(token.get('id')), int(request.args.get('user_id')))
        return get_all_json_users()
    except TokenAuthError as e:
        return create_response(Status.FAILED, 'Token authentication failed', e)
    except ResourceNotFoundError as e:
        return create_response(Status.FAILED, 'Resource was not found', e)


@app.route('/user', methods=['POST'])
def user_post():
    username = request.get_json()['username']
    email = request.get_json()['email']
    password = request.get_json()['password']
    if username and email and password:
        new_user = create_user(username, email, password)
        return create_response(Status.SUCCESS, 'User created')
    return create_response(Status.FAILED, 'Failed to create user, some params not set')


@app.route('/user/login', methods=['POST'])
def user_login():
    username = request.get_json()['username']
    password = request.get_json()['password']
    new_jwt = login_user(username, password)
    if not new_jwt:
        return create_response(Status.FAILED, 'Authentication failed, username and/or password not correct')
    return create_login_success_response(new_jwt)

