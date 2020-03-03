from flask import request, render_template, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app
from .workout_model import Workout
from .workout_controller import create_workout, get_all_json_workouts
from .. import db

@app.route('/workout', methods=['GET', 'POST'])
def workout_root():
    if request.method == 'GET':
        return get_all_json_workouts()
    elif request.method == 'POST':
        json_req = request.get_json()
        if 'workout_name' in json_req and 'workout_type' in json_req:
            workout_name = json_req['workout_name']
            workout_type = json_req['workout_type']
            workout_at = json_req['workout_at'] if 'workout_at' in json_req else None
            new_workout = create_workout(workout_name, workout_type, workout_at)
            return make_response(f'{new_workout} successfully created')
        return make_response(f'Failed to create workout.. workout_name {workout_name} workout_type {workout_type}')
    
