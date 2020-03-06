from datetime import datetime as dt
from sqlalchemy.exc import SQLAlchemyError

from workin_api import db
from workin_api.workout_entry.workout_entry_model import WorkoutEntry


def create_workout_entry(entry_type, amount_per_set, num_sets, weight, duration, workout_id):
    try:
        new_workout_entry = WorkoutEntry(created=dt.now(),
                                         entry_type=entry_type,
                                         amount_per_set=amount_per_set,
                                         num_sets=num_sets,
                                         weight=weight,
                                         duration=duration,
                                         workout_id=workout_id)
        db.session.add(new_workout_entry)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return new_workout_entry
    except SQLAlchemyError as e:
        print('got sqlalchemy error:', str(e))
        raise
    except Exception as e:
        print('got general error:', str(e))
        raise

