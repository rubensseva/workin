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

    def to_dict(self):
        return {
                'id': self.id,
                'username': self.username,
                'workouts': [
                {
                    'id': workout.id,
                    'name': workout.name,
                    'is_completed': workout.is_completed,
                    'created': workout.created,
                    'workout_at': workout.workout_at,
                    'workout_duration': workout.workout_duration,
                    'workout_type': workout.workout_type,
                    'workout_entries': [
                        {
                            'id': entry.id,
                            'entry_type': entry.entry_type,
                            'amount_per_set': entry.amount_per_set,
                            'num_sets': entry.num_sets
                        }
                        for entry in workout.workout_entries
                    ]
                }
                for workout in self.workouts
                ]
            }
