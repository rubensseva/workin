from flask import request

from flask import current_app as app
from workin_api.shared.auth_controller import authorize
from workin_api.shared.exceptions import TokenAuthError, ResourceNotFoundError
from workin_api.shared.utils import create_response, create_login_success_response, Status
from workin_api.user.user_controller import create_user, get_users, get_personal_data, login_user


@app.route('/user', methods=['GET'])
def user_get():
    try:
        token = authorize()
        if 'user_id' in request.args:
            return get_personal_data(
                int(token.get('id')), int(request.args.get('user_id')))
        if 'user_id' in request.args or 'username' in request.args or 'email' in request.args:
            return create_response('User found', Status.SUCCESS, 200, payload=get_users(request.args.get('user_id'), request.args.get('username'), request.args.get('email')))
    except TokenAuthError as e:
        return create_response('Token authentication failed', Status.FAILED, 401, e)
    except ResourceNotFoundError as e:
        return create_response('Resource was not found', Status.FAILED, 404, e)


@app.route('/user', methods=['POST'])
def user_post():
    username = request.get_json()['username']
    email = request.get_json()['email']
    password = request.get_json()['password']
    if username and email and password:
        new_user = create_user(username, email, password)
        return create_response('User created', Status.SUCCESS, 200)
    return create_response('Failed to create user, some params not set', Status.FAILED, 422)


@app.route('/user/verify_token', methods=['GET'])
def user_verify_token():
    try: 
        token = authorize()
        user = get_users(id=token.get('id'))[0]
        return create_response('Token verification success', Status.SUCCESS, 200, payload=user)
    except TokenAuthError as e:
        return create_response('Token verification failed', Status.FAILED, 401)
    except IndexError as e:
        return create_response('Could not recognize user id of token', Status.FAILED, 500)



@app.route('/user/login', methods=['POST'])
def user_login():
    username = request.get_json()['username']
    password = request.get_json()['password']
    new_jwt = login_user(username, password)
    if not new_jwt:
        return create_response('Authentication failed, username and/or password not correct', Status.FAILED, 401)
    return create_login_success_response(new_jwt)

