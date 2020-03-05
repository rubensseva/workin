from datetime import datetime as dt, timedelta
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError
import jwt
from passlib.hash import sha256_crypt

from workin_api import db
from workin_api.user.user_model import User
from workin_api.shared.exceptions import ResourceNotFoundError


def create_user(username, email, password):
    try:
        password_hash = sha256_crypt.encrypt(password)
        new_user = User(username=username,
                        password_hash=password_hash,
                        email=email,
                        created=dt.now(),
                        admin=False)
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return new_user
    except SQLAlchemyError as e:
        print('got sqlalchemy error:', str(e))
        raise
    except Exception as e:
        print('got general error:', str(e))
        raise


def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        print(f'user {username} does not exist...')
        return None
    if verify_password_hash(password, user.password_hash):
        return get_user_jwt(user.id)
    print('user password did not match hash...')
    return None


def verify_password_hash(password, password_hash):
    return sha256_crypt.verify(password, password_hash)


def get_user_jwt(userid):
    encoded_jwt = jwt.encode({'id': userid, 'exp': dt.timestamp(
        dt.utcnow() + timedelta(hours=3))}, 'secret', algorithm='HS256').decode('utf-8')
    return encoded_jwt


def verify_jwt(token):
    try:
        decoded_jwt_obj = jwt.decode(token, 'secret', algorithm='HS256')
        return decoded_jwt_obj
    except jwt.InvalidSignatureError:
        print('got invalid signature error when handling jwt')
        raise Exception('jwt signature error')
    except jwt.DecodeError:
        print('got decode error when handling jwt')
        raise Exception('jwt token was not valid')
    except jwt.ExpiredSignatureError:
        print('got expiredsignature error')
        raise Exception('jwt expired')
    except BaseException:
        print('got general error when handling jwt')
        raise Exception('jwt irregular error')


def get_all_json_users():
    users = User.query.all()
    return jsonify([
        {
            'id': user.id,
            'username': user.username,
        }
        for user in users
    ])


def get_users(id=None, username=None, email=None):
    filter_data = {'id': id, 'username': username, 'email': email}
    filter_data = {key: value for (key, value) in filter_data.items()
               if value}
    users = User.query.filter_by(**filter_data).all()
    user_dicts = [user.to_dict() for user in users]
    return user_dicts


def get_personal_data(user_id_logged_in, user_id_to_fetch):
    user = User.query.filter_by(id=user_id_to_fetch).first()
    if not user:
        raise ResourceNotFoundError(
            user_id_to_fetch,
            'Could not find any user by provided id')
    if user_id_logged_in == user_id_to_fetch:
        return jsonify({
            'id': user.id,
            'username': user.username,
            'admin': user.admin,
            'created': user.created,
            'email': user.email,
            'password_hash': user.password_hash
        })
    return jsonify({
        'id': user.id,
        'username': user.username,
    })
