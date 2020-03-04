from flask import jsonify
from enum import Enum, auto


class Status(Enum):
    SUCCESS = auto()
    FAILED = auto()


STATUS_MAP = {
    Status.SUCCESS: 'success',
    Status.FAILED: 'failed'
}


def create_response(status, message, err=None):
    response = {'status': STATUS_MAP[status], 'msg': message}
    if err:
        response['err'] = str(err)
    return jsonify(response)

def create_login_success_response(token):
    response = {'status': STATUS_MAP[Status.SUCCESS], 'msg': 'Authentication success', 'jwt': token}
    return jsonify(response)
