from .. import db

class WorkoutEntry(db.Model):
    """Model for workout entries."""
    __tablename__ = 'workout_entries'
    id = db.Column(db.Integer,
                        primary_key=True)
    entry_type = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    amount_per_set = db.Column(db.Integer,
                        index=False,
                        unique=False,
                        nullable=False)
    num_sets = db.Column(db.Integer,
                        index=False,
                        unique=False,
                        nullable=False)
    workout_id = db.Column(db.Integer,
                        db.ForeignKey('workouts.id'),
                        index=False,
                        unique=False,
                        nullable=False)
