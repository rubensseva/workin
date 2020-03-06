from datetime import datetime as dt
from sqlalchemy.exc import SQLAlchemyError

from workin_api import db
from workin_api.workout_plan.workout_plan_model import WorkoutPlan


def create_workout_plan(name, week_day_start, user_id):
    try:
        new_workout_plan = WorkoutPlan(created=dt.now(),
                                       name=name,
                                       week_day_start=week_day_start,
                                       user_id=user_id)
        db.session.add(new_workout_plan)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return new_workout_plan
    except SQLAlchemyError as e:
        print('got sqlalchemy error:', str(e))
        raise
    except Exception as e:
        print('got general error:', str(e))
        raise
