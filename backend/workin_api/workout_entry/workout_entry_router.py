from flask import request, make_response
from flask import current_app as app
from workin_api.workout_entry.workout_entry_controller import create_workout_entry, get_all_json_workout_entries
from workin_api.shared.auth_helpers import require_auth
from workin_api import db

@app.route('/workout_entry', methods=['GET', 'POST'])
@require_auth
def workout_entry_root():
    if request.method == 'GET':
        return get_all_json_workout_entries()
    elif request.method == 'POST':
        json_req = request.get_json()
        if 'type' in json_req and 'amount_per_set' in json_req and 'num_sets' in json_req and 'workout_id' in json_req:
            entry_type = json_req['type']
            amount_per_set = json_req['amount_per_set']
            num_sets = json_req['num_sets']
            workout_id = json_req['workout_id']
            new_workout_entry = create_workout_entry(entry_type, amount_per_set, num_sets, workout_id)
            return make_response(f'{new_workout_entry} successfully created')
        return make_response(f'Failed to create workout entry.. request obj: {json_req}')
    
