from flask import jsonify
from datetime import datetime as dt

from .. import db
from .workout_model import Workout

def create_workout(name, w_type, at):
    if not at:
        at = dt.now()
    new_workout = Workout(workout_name=name,
                    workout_type=w_type,
                    created=dt.now(),
                    workout_at=at)
    db.session.add(new_workout)  # Adds new User record to database
    db.session.commit()  # Commits all changes
    return new_workout

def get_all_json_workouts():
    workouts = Workout.query.all()
    workout_dicts = [
        {
            'id': workout.id,
            'workout_name': workout.workout_name,
            'workout_type': workout.workout_type,
            'created': workout.created,
        }
        for workout in workouts
    ]
    print(workout_dicts)
    return jsonify(workout_dicts)
