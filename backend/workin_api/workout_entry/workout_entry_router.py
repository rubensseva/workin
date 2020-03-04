from flask import request, make_response

from flask import current_app as app
from workin_api.workout_entry.workout_entry_controller import create_workout_entry, get_all_json_workout_entries
from workin_api.shared.auth_controller import authorize
from workin_api.shared.exceptions import TokenAuthError, ResourceNotFoundError
from workin_api.shared.utils import create_response, Status
from workin_api import db


@app.route('/workout_entry', methods=['GET'])
def workout_entry_get():
    try:
        authorize()
        return create_response(Status.SUCCESS, get_all_json_workout_entries())
    except TokenAuthError as e:
        return create_response(Status.FAILED, 'Token authentication failed', e)

@app.route('/workout_entry', methods=['POST'])
def workout_entry_post():
    try:
        authorize()
        json_req = request.get_json()
        if 'type' not in json_req or 'amount_per_set' not in json_req or 'num_sets' not in json_req or 'workout_id' not in json_req:
            return create_response(Status.FAILED, 'Missing param when attempting to create workout entry')
        entry_type = json_req['type']
        amount_per_set = json_req['amount_per_set']
        num_sets = json_req['num_sets']
        workout_id = json_req['workout_id']
        new_workout_entry = create_workout_entry(
            entry_type, amount_per_set, num_sets, workout_id)
        return create_response(Status.SUCCESS, 'Workout entry created')
    except TokenAuthError as e:
        return create_response(Status.FAILED, 'Token authentication failed', e)
