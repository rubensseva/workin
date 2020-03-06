from flask import request, render_template, make_response, jsonify
from datetime import datetime as dt
import dateutil.parser
from flask import current_app as app
from workin_api.shared.auth_controller import authorize
from workin_api.shared.exceptions import TokenAuthError, ResourceNotFoundError
from workin_api.workout.workout_model import Workout
from workin_api.workout.workout_controller import create_workout, get_all_json_workouts, get_user_workouts
from workin_api.shared.utils import create_response, Status
from workin_api import db


@app.route('/workout', methods=['GET'])
def workout_get():
    try:
        token = authorize()
        print('token:', token)
        return create_response(get_user_workouts(token.get('id')), Status.SUCCESS, 200)
    except TokenAuthError as e:
        return create_response('Token authentication failed', Status.FAILED, 401, e)


@app.route('/workout', methods=['POST'])
def workout_post():
    try:
        authorize()
        json_req = request.get_json()
        if 'name' in json_req and 'workout_type' in json_req and 'user_id' in json_req:
            name = json_req['name']
            is_completed = json_req['is_completed'] if 'is_completed' in json_req else None
            workout_type = json_req['workout_type']
            workout_at = dateutil.parser.isoparse(json_req['workout_at']) if 'workout_at' in json_req else None
            workout_duration = json_req['workout_duration'] if 'workout_duration' in json_req else None
            user_id = json_req['user_id']
            new_workout = create_workout(
                name, is_completed, user_id, workout_at, workout_duration, workout_type)
            return create_response('Workout created', Status.SUCCESS, 200)
        return create_response('Failed to create workout, required params was missing', Status.FAILED, 422)
    except TokenAuthError as e:
        return create_response('Token authentication failed', Status.FAILED, 401, e)
