from app import api
from app.API.MaintenanceAPI import MaintenanceAPI
from app.API.ShiftManagerAPI import ShiftManagerAPI
from app.API.UserAPI import UserApi

api.add_resource(MaintenanceAPI, "/maintenance", "/maintenance/<string:worker_id>")
api.add_resource(ShiftManagerAPI, "/management", "/management/<string:shift_id>")
api.add_resource(UserApi, "/user", "/user/<string:worker_id>")

