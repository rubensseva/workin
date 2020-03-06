from workin_api import db


class Workout(db.Model):
    """Model for workouts."""

    __tablename__ = 'workouts'
    id = db.Column(db.Integer,
                   primary_key=True)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    name = db.Column(db.String(64),
                     index=False,
                     unique=False,
                     nullable=False)
    is_completed = db.Column(db.Boolean,
                             index=False,
                             unique=False,
                             nullable=False)
    is_template = db.Column(db.Boolean,
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
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        index=False,
                        unique=False,
                        nullable=False)
    workout_plan_id = db.Column(db.Integer,
                        db.ForeignKey('workout_plans.id'),
                        index=False,
                        unique=False,
                        nullable=True)
    workout_entries = db.relationship('WorkoutEntry')


    def to_dict(self):
        return {
                'id': self.id,
                'created': self.created,
                'name': self.name,
                'is_completed': self.is_completed,
                'is_template': self.is_template,
                'created': self.created,
                'workout_at': self.workout_at,
                'workout_duration': self.workout_duration,
                'workout_type': self.workout_type,
                'user_id': self.user_id,
                'workout_plan_id': self.workout_plan_id,
                'workout_entries': [
                    workout_entry.to_dict()
                    for workout_entry in self.workout_entries
                ]
            }
