from workin_api import db


class Workout(db.Model):
    """Model for workouts."""

    __tablename__ = 'workouts'
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(64),
                     index=False,
                     unique=False,
                     nullable=False)
    is_completed = db.Column(db.Boolean,
                             index=False,
                             unique=False,
                             nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        index=False,
                        unique=False,
                        nullable=False)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    workout_at = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)
    workout_duration = db.Column(db.Integer,
                           index=False,
                           unique=False,
                           nullable=True)
    workout_type = db.Column(db.String(64),
                             index=False,
                             unique=False,
                             nullable=False)
    workout_entries = db.relationship('WorkoutEntry')
