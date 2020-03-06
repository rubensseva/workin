from workin_api import db


class User(db.Model):
    """Model for user accounts."""

    __tablename__ = 'users'
    id = db.Column(db.Integer,
                   primary_key=True)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
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
    admin = db.Column(db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)
    workouts = db.relationship('Workout')
    workout_plans = db.relationship('WorkoutPlan')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def to_dict(self):
        return {
                'id': self.id,
                'created': self.created,
                'username': self.username,
                'workouts': [
                    workout.to_dict()
                    for workout in self.workouts
                ],
                'workout_plans': [
                    workout_plan.to_dict()
                    for workout_plan in self.workout_plans
                ]
            }
