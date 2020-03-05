from flask import jsonify, make_response
from enum import Enum, auto


class Status(Enum):
    SUCCESS = auto()
    FAILED = auto()


STATUS_MAP = {
    Status.SUCCESS: 'success',
    Status.FAILED: 'failed'
}


def create_response(message, status, status_code, err=None):
    response = {'status': STATUS_MAP[status], 'msg': message}
    if err:
        response['err'] = str(err)
    return make_response(jsonify(response), status_code)

def create_login_success_response(token):
    response = {'status': STATUS_MAP[Status.SUCCESS], 'msg': 'Authentication success', 'jwt': token}
    return make_response(jsonify(response), 200)
