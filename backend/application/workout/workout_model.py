from .. import db

class Workout(db.Model):
    """Model for workouts."""
    __tablename__ = 'workouts'
    id = db.Column(db.Integer,
                        primary_key=True)
    workout_name = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    workout_at = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    workout_type = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
