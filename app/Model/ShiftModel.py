import uuid
from app import db
from app.Resource.all_resources import Shift, Worker
from app.db_functions import commit_or_abort, terminate_request


class ShiftModel:

    def __init__(self, shift_id=None):
        self.uuid = shift_id if shift_id else str(uuid.uuid4())
        self._shift = Shift.get_shift_by_uuid(self.uuid) if shift_id else None

    @property
    def shift(self):
        return self._shift

    def create_shift(self, worker_id, shift_time, shift_date):
        self._shift = Shift(id=self.uuid, worker_id=worker_id, shift_time=shift_time, shift_date=shift_date)
        db.session.add(self._shift)
        db.session.commit()
        # commit_or_abort('ERR_SHIFT_CREATION_FAILED', 400)
        return self._shift

    def delete_shift(self):
        if not self._shift:
            return {'error': 'ERR_SHIFT_NOT_FOUND'}, 404
        db.session.delete(self._shift)
        commit_or_abort(({'error': 'ERR_SHIFT_DELETION_FAILED'}, 500))
        return {'status': 'OK'}, 200

    def update_shift_time(self, shift_time):
        self._shift.shift_time = shift_time
        commit_or_abort(({'error': 'ERR_SHIFT_UPDATE_FAILED'}, 500))
        return self._shift

    def update_shift_date(self, shift_date):
        self._shift.shift_date = shift_date
        commit_or_abort(({'error': 'ERR_SHIFT_UPDATE_FAILED'}, 500))
        return self._shift

    def check_if_shift_exists(self, shift_date, shift_time, worker_id):
        shift = Shift.get_shift_by_worker_id_shift_time_shift_date(shift_date=shift_date, shift_time=shift_time, worker_id=worker_id)
        shift_in_the_day = Shift.get_shift_by_worker_id_shift_date(worker_id=worker_id, shift_date=shift_date
                                                                   )
        if shift or shift_in_the_day:
            terminate_request(406, "SHIFT_ALREADY_EXISTS")

    def get_shifts_by_worker_id(self, worker_id):
        shifts = Shift.get_shifts_by_worker_id(worker_id=worker_id)
        result = []

        for elem in shifts:
            elem_dict = {'id': elem.id,
                         'shift_time': elem.shift_time.name,
                         'shift_date': elem.shift_date,
                         'worker': {'worker_id': elem.worker_id,
                                    'name': Worker.get_worker_by_uuid(elem.worker_id).name,
                                    'surname': Worker.get_worker_by_uuid(elem.worker_id).surname,
                                    'position': Worker.get_worker_by_uuid(elem.worker_id).position}}
            result.append(elem_dict)
        return result

    def get_all_shifts(self):
        shifts = Shift.get_all_shifts()
        result = []

        for elem in shifts:
            elem_dict = {'id': elem.id,
                         'shift_time': elem.shift_time.name,
                         'shift_date': elem.shift_date,
                         'worker': {'worker_id': elem.worker_id,
                                    'name': Worker.get_worker_by_uuid(elem.worker_id).name,
                                    'surname': Worker.get_worker_by_uuid(elem.worker_id).surname,
                                    'position': Worker.get_worker_by_uuid(elem.worker_id).position}}
            result.append(elem_dict)
        return result
