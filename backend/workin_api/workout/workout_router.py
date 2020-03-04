from flask import request, render_template, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app
from workin_api.workout.workout_model import Workout
from workin_api.workout.workout_controller import create_workout, get_all_json_workouts
from workin_api import db

@app.route('/workout', methods=['GET', 'POST'])
def workout_root():
    if request.method == 'GET':
        return get_all_json_workouts()
    elif request.method == 'POST':
        json_req = request.get_json()
        if 'name' in json_req and 'workout_type' in json_req and 'user_id' in json_req and 'workout_id' in json_req:
            name = json_req['name']
            is_completed = json_req['is_completed'] if 'is_completed' in json_req else None
            workout_type = json_req['workout_type']
            workout_at = json_req['workout_at'] if 'workout_at' in json_req else None
            user_id = json_req['user_id']
            workout_id = json_req['workout_id']
            new_workout = create_workout(name, is_completed, user_id, workout_at, workout_type)
            return make_response(f'{new_workout} successfully created')
        return make_response(f'Failed to create workout.. workout_name {workout_name} workout_type {workout_type}')
    
