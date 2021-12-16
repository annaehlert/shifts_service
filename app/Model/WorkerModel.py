import uuid
from app import db
from app.Resource.all_resources import Worker
from app.db_functions import commit_or_abort


class WorkerModel:

    def __init__(self, worker_id=None):
        self.uuid = worker_id if worker_id else str(uuid.uuid4())
        self._worker = Worker.get_worker_by_uuid(self.uuid) if worker_id else None

    @property
    def worker(self):
        return self._worker

    def create_worker(self, name, surname, position):
        self._worker = Worker(id=self.uuid, name=name, surname=surname, position=position)
        db.session.add(self._worker)
        commit_or_abort('ERR_WORKER_CREATION_FAILED', 400)
        return self._worker

    def delete_worker(self):
        if not self._worker:
            return {'error': 'ERR_WORKER_NOT_FOUND'}, 404
        db.session.delete(self._worker)
        commit_or_abort(({'error': 'ERR_WORKER_DELETION_FAILED'}, 500))
        return {'status': 'OK'}, 200

    def update_worker_name(self, name):
        self._worker.name = name
        commit_or_abort(({'error': 'ERR_WORKER_UPDATE_FAILED'}, 500))
        return self._worker

    def update_worker_surname(self, surname):
        self._worker.surname = surname
        commit_or_abort(({'error': 'ERR_WORKER_UPDATE_FAILED'}, 500))
        return self._worker

    def update_worker_position(self, position):
        self._worker.position = position
        commit_or_abort(({'error': 'ERR_WORKER_UPDATE_FAILED'}, 500))
        return self._worker

    def get_all_workers(self):
        return Worker.get_all_workers()

    def get_worker_by_uuid(self, worker_id):
        return Worker.get_worker_by_uuid(worker_id)

    def get_worker_by_name_and_surname(self, name, surname):
        return (Worker.get_worker_by_name_and_surname(name=name, surname=surname)).id
