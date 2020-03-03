from flask import jsonify
from datetime import datetime as dt
from passlib.hash import sha256_crypt

from .. import db
from .user_model import User

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


def verify_user_password(username, password):
    user = User.query.filter(username=username)
    return sha256_crypt.verify(password, user.password_hash))


def get_all_json_users():
    users = User.query.all()
    return jsonify([
        {
            'id': user.id,
            'username': user.username,
            'admin': user.admin,
            'created': user.created,
            'email': user.email,
        }
        for user in users
    ])
    
