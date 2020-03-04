from datetime import datetime as dt
from flask import jsonify

from workin_api import db
from workin_api.workout_entry.workout_entry_model import WorkoutEntry

def create_workout_entry(entry_type, amount_per_set, num_sets, workout_id):
    new_workout_entry = WorkoutEntry(entry_type=entry_type,
                                     amount_per_set=amount_per_set,
                                     num_sets=num_sets,
                                     workout_id=workout_id)
    db.session.add(new_workout_entry)  # Adds new User record to database
    db.session.commit()  # Commits all changes
    return new_workout_entry

def get_all_json_workout_entries():
    workout_entries = WorkoutEntry.query.all()
    workout_entries_dicts = [
        {
            'id': workout_entry.id,
            'entry_type': workout_entry.entry_type,
            'amount_per_set': workout_entry.amount_per_set,
            'num_sets': workout_entry.num_sets,
        }
        for workout_entry in workout_entries
    ]
    print(workout_entries_dicts)
    return jsonify(workout_entries_dicts)
