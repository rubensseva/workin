from .. import db


class WorkoutEntry(db.Model):
    """Model for workout entries."""
    __tablename__ = 'workout_entries'
    id = db.Column(db.Integer,
                   primary_key=True)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    entry_type = db.Column(db.String(64),
                           index=False,
                           unique=False,
                           nullable=False)
    amount_per_set = db.Column(db.Integer,
                               index=False,
                               unique=False,
                               nullable=False)
    num_sets = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)
    duration = db.Column(db.Integer,
                          index=False,
                          unique=False,
                          nullable=True)
    weight = db.Column(db.Integer,
                          index=False,
                          unique=False,
                          nullable=True)
    workout_id = db.Column(db.Integer,
                           db.ForeignKey('workouts.id'),
                           index=False,
                           unique=False,
                           nullable=False)
 
    def to_dict(self):
        return {
            'id': self.id,
            'created': self.created,
            'entry_type': self.entry_type,
            'amount_per_set': self.amount_per_set,
            'num_sets': self.num_sets,
            'duration': self.duration,
            'weight': self.weight,
            'workout_id': self.workout_id
        }
