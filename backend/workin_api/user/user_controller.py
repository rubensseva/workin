from datetime import datetime as dt, timedelta
from flask import jsonify
import jwt
from passlib.hash import sha256_crypt

from workin_api import db
from workin_api.user.user_model import User

def create_user(username, email, password):
    password_hash = sha256_crypt.encrypt(password)
    new_user = User(username=username,
                    password_hash=password_hash,
                    email=email,
                    created=dt.now(),
                    admin=False)
    db.session.add(new_user)  # Adds new User record to database
    db.session.commit()  # Commits all changes
    return new_user

def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        print(f'user {username} does not exist...')
        return None
    if (verify_password_hash(password, user.password_hash)):
        return get_user_jwt(user.id)
    print('user password did not match hash...')
    return None

def verify_password_hash(password, password_hash):
    return sha256_crypt.verify(password, password_hash)

def get_user_jwt(userid):
    encoded_jwt = jwt.encode({'id': userid, 'exp': (dt.utcnow() + timedelta(hours=3)).timestamp()}, 'secret', algorithm='HS256').decode('utf-8')
    return encoded_jwt

def verify_jwt(token):
    try:
        decoded_jwt_obj = jwt.decode(token, 'secret', algorithm='HS256')
        return decoded_jwt_obj
    except jwt.DecodeError:
        print('got decode error when handling jwt')
    except jwt.InvalidSignatureError:
        print('got invalid signature error when handling jwt')
    except jwt.ExpiredSignatureError:
        print('got expiredsignature error')
    except:
        print('got general error when handling jwt')

def get_all_json_users():
    users = User.query.all()
    return jsonify([
        {
            'id': user.id,
            'username': user.username,
            'admin': user.admin,
            'created': user.created,
            'email': user.email,
            'password_hash': user.password_hash
        }
        for user in users
    ])
