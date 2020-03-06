from flask import request

from flask import current_app as app
from workin_api.workout_entry.workout_entry_controller import create_workout_entry
from workin_api.shared.auth_controller import authorize
from workin_api.shared.exceptions import TokenAuthError
from workin_api.shared.utils import create_response, Status


@app.route('/workout_entry', methods=['POST'])
def workout_entry_post():
    try:
        authorize()
        json_req = request.get_json()
        if 'type' not in json_req or 'amount_per_set' not in json_req or 'num_sets' not in json_req or 'workout_id' not in json_req:
            return create_response('Missing param when attempting to create workout entry', Status.FAILED, 422)
        entry_type = json_req['type']
        amount_per_set = json_req['amount_per_set']
        num_sets = json_req['num_sets']
        duration = json_req['duration'] if 'duration' in json_req else None
        weight = json_req['weight'] if 'weight' in json_req else None
        workout_id = json_req['workout_id']
        new_workout_entry = create_workout_entry(
            entry_type, amount_per_set, num_sets, weight, duration, workout_id)
        return create_response('Workout entry created', Status.SUCCESS, 200)
    except TokenAuthError as e:
        return create_response('Token authentication failed', Status.FAILED, 401, e)
