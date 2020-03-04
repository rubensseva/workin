from flask import request, jsonify
from workin_api.shared.auth_helpers import decode_token, extract_token
from workin_api.shared.exceptions import TokenAuthError

def authorize():
    try:
        unverified_token = extract_token(request)
        return decode_token(unverified_token)
    except Exception as e:
        print('Token authentication failed')
        raise TokenAuthError(e, 'Token authentiation failed')
