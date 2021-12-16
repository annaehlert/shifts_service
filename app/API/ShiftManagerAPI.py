from flask_restful import Resource
import json
from app.Model.ShiftModel import ShiftModel
from app.Model.WorkerModel import WorkerModel
from app.Resource.all_resources import Worker
from app.schema.all_schemas import shift_schema, shift_result_schema
from flask import request


class ShiftManagerAPI(Resource):
    '''
    without parameter worker_id you can get all shifts
    with parameter worker_id you get all data of specific worker
    '''

    def get(self):
        worker_id = request.args.get('worker_id', None)
        if not worker_id:
            shifts = ShiftModel().get_all_shifts()
            return shifts
        else:
            worker = Worker.get_worker_by_uuid(worker_id)
            shifts = ShiftModel().get_shifts_by_worker_id(worker_id=worker_id)
            return shifts

    def post(self):
        try:
            message = request.get_json()
            if not message:
                message = json.loads(request.get_data())
        except Exception as e:
            return {'error': e}, 400
        errors = shift_schema.validate(message)
        if errors:
            return errors, 400
        worker_id = message.get('worker_id')
        shift_time = message.get('shift_time')
        shift_date = message.get('shift_date')
        ShiftModel().check_if_shift_exists(worker_id=worker_id, shift_time=shift_time, shift_date=shift_date)
        final_shift = ShiftModel().create_shift(worker_id=worker_id, shift_date=shift_date, shift_time=shift_time)
        return shift_result_schema.dump(final_shift)

    def patch(self, shift_id):
        try:
            message = request.get_json()
            if not message:
                message = json.loads(request.get_data())
        except:
            return {'status': 'ERR_BAD_REQUEST'}, 400
        shift_time = message.get('shift_time', None)
        shift_date = message.get('shift_date', None)
        if shift_time:
            ShiftModel(shift_id).update_shift_time(shift_time=shift_time)
        if shift_date:
            ShiftModel(shift_id).update_shift_date(shift_date=shift_date)
        return shift_schema.dump(ShiftModel(shift_id))

    def delete(self, shift_id):
        return ShiftModel(shift_id).delete_shift()
