from workin_api import db

class User(db.Model):
    """Model for user accounts."""

    __tablename__ = 'users'
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(64),
                        index=False,
                        unique=True,
                        nullable=False)
    password_hash = db.Column(db.String(256),
                        index=False,
                        nullable=False)
    email = db.Column(db.String(80),
                        index=True,
                        unique=True,
                        nullable=False)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    admin = db.Column(db.Boolean,
                        index=False,
                        unique=False,
                        nullable=False)
    workouts = db.relationship('Workout')

    def __repr__(self):
        return '<User {}>'.format(self.username)
