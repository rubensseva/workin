from flask import request, jsonify
from flask import current_app as app
from workin_api.shared.auth_controller import authorize
from workin_api.shared.exceptions import TokenAuthError, ResourceNotFoundError
from workin_api.shared.utils import create_response, Status

from workin_api.user.user_controller import create_user, get_all_json_users, get_personal_data, login_user


@app.route('/user', methods=['GET'])
def user_root():
    try:
        token = authorize()
        if 'user_id' in request.args:
            return get_personal_data(int(token.get('id')), int(request.args.get('user_id')))
        return get_all_json_users()
    except TokenAuthError as e:
        return create_response(Status.FAILED, 'Token authentication failed', e)
    except ResourceNotFoundError as e:
        return create_response(Status.FAILED, 'Resource was not found', e)
    except Exception as e:
        raise

@app.route('/user', methods=['POST'])
def user_post():
    username = request.get_json()['username']
    email = request.get_json()['email']
    password = request.get_json()['password']
    if username and email and password:
        try:
            new_user = create_user(username, email, password)
            return jsonify({'status': 'success', 'msg': f'{new_user} successfully created!'})
        except Exception as e:
            print('Error occured', str(e))
            return jsonify({'status': 'failed', 'msg': 'Error occured when attempting to create user', 'err': str(e)})
    return jsonify({'status': 'failed', 'msg': f"failed to create user, some required params not set. Request obj: {request.get_json()}"})


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
