from flask_restful import Resource

from app.Model.WorkerModel import WorkerModel
from app.schema.all_schemas import worker_schema


class UserApi(Resource):
    '''
    without parameter worker_id you can get all users
    with parameter worker_id you get all data of specific worker
    '''

    def get(self, worker_id=None):
        if not worker_id:
            workers = WorkerModel().get_all_workers()
            workers_list = []
            for elem in workers:
                workers_list.append(worker_schema.dump(elem))
            return workers_list
        worker = WorkerModel().get_worker_by_uuid(worker_id)
        return worker_schema.dump(worker)

    def delete(self, worker_id):
        return WorkerModel(worker_id).delete_worker()
