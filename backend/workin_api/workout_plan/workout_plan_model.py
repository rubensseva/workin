from workin_api import db


class WorkoutPlan(db.Model):
    """Model for workout plans."""

    __tablename__ = 'workout_plans'
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
    week_day_start = db.Column(db.Integer,
            index=False,
            unique=False,
            nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        index=False,
                        unique=False,
                        nullable=False)
    workouts = db.relationship('Workout')

    def to_dict(self):
        return {
                'id': self.id,
                'created': self.created,
                'name': self.username,
                'week_day_start': self.week_day_start,
                'user_id': self.user_id,
                'workouts': [
                    workout.to_dict()
                    for workout in self.workouts
                ]
        }
