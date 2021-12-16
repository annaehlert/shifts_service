from flask_restful import Resource
from app.Model.WorkerModel import WorkerModel
from app.db_functions import create_database
from app.schema.all_schemas import worker_schema
from flask import request, json, Response


class MaintenanceAPI(Resource):

    def get(self):
        return create_database()

    def post(self):
        try:
            message = request.get_json()
            if not message:
                message = json.loads(request.get_data())
        except Exception as e:
            return {'error': e}, 400
        errors = worker_schema.validate(message)
        if errors:
            return errors, 400
        name = message.get('name')
        surname = message.get('surname')
        position = message.get('position')
        worker = WorkerModel().create_worker(name=name, surname=surname, position=position)
        return worker_schema.dump(worker)

    def patch(self, worker_id):
        try:
            message = request.get_json()
            if not message:
                message = json.loads(request.get_data())
        except:
            return {'status': 'ERR_BAD_REQUEST'}, 400
        name = message.get('name', None)
        surname = message.get('surname', None)
        position = message.get('position', None)
        if name:
            WorkerModel(worker_id).update_worker_name(name=name)
        if surname:
            WorkerModel(worker_id).update_worker_surname(surname=surname)
        if position:
            WorkerModel(worker_id).update_worker_position(position=position)
        return worker_schema.dump(WorkerModel(worker_id).worker)
