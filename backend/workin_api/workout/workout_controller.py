from datetime import datetime as dt
from sqlalchemy.exc import SQLAlchemyError

from workin_api import db
from workin_api.workout.workout_model import Workout


def create_workout(name, is_completed, user_id, workout_at, workout_duration, workout_type):
    try:
        if not workout_at:
            workout_at = None
        if not workout_duration:
            workout_duration = None
        if not is_completed:
            is_completed = False
        is_template = False
        new_workout = Workout(created=dt.now(),
                              name=name,
                              is_completed=is_completed,
                              is_template=is_template,
                              workout_at=workout_at,
                              workout_duration=workout_duration,
                              workout_type=workout_type,
                              user_id=user_id)
        db.session.add(new_workout)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return new_workout
    except SQLAlchemyError as e:
        print('Got sqlalchemy error:', str(e))
        raise
