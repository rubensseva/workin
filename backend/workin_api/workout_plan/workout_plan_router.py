from flask import request

from flask import current_app as app
from workin_api.workout_plan.workout_plan_controller import create_workout_plan
from workin_api.shared.auth_controller import authorize
from workin_api.shared.exceptions import TokenAuthError
from workin_api.shared.utils import create_response, Status


@app.route('/workout_plan', methods=['POST'])
def workout_plan_post():
    try:
        authorize()
        json_req = request.get_json()
        if 'name' not in json_req or 'week_day_start' not in json_req or 'user_id' not in json_req:
            return create_response('Missing param when attempting to create workout plan', Status.FAILED, 422)
        name = json_req['name']
        week_day_start = json_req['week_day_start']
        user_id = json_req['user_id']
        new_workout_plan = create_workout_plan(
            name, week_day_start, user_id)
        return create_response('Workout plan created', Status.SUCCESS, 200)
    except TokenAuthError as e:
        return create_response('Token authentication failed', Status.FAILED, 401, e)
