import sys
from flask import request, jsonify

def require_auth(func):
    """
        This is a decorator function to enable safe and secure endpoints
        Use this on any flask route that should require auth jwt token
    """
    def wrapper():
        print("Something is happening before the function is called.")
        print(request.headers.get('Authorization'))
        unverified_token = request.headers.get('Authorization').split(' ')[1]
        print(unverified_token)
        print(request.get_json())
        try:
            decoded_jwt_obj = verify_jwt(unverified_token)
        except Exception as e:
            print("Unexpected error:", sys.exc_info()[0])
            print('login failed!')
            return failed_login(e)
        print("Something is happening after the function is called.")
        print('got token', decoded_jwt_obj)
        print('Auth considered successful')
        return func()
    return wrapper

def failed_login(err):
    return jsonify({'status': 'Failed', 'msg': 'Token was not valid, login failed', 'err': str(err)})

