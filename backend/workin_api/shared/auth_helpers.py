import sys
from flask import request, jsonify
from workin_api.user.user_controller import verify_jwt

def extract_token(request_obj):
    try:
        return request.headers.get('Authorization').split(' ')[1]
    except:
        print('Couldnt parse auth token in http header')
        raise

def decode_token(unverified_token):
    print("Authenticating token...")
    print(unverified_token)
    try:
        decoded_jwt_obj = verify_jwt(unverified_token)
        print('got token', decoded_jwt_obj)
        print('Auth considered successful')
        return decoded_jwt_obj
    except Exception as e:
        print("Unexpected error:", str(e))
        print('login failed!')
        raise
