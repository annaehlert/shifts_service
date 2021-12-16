from marshmallow import fields, Schema
from marshmallow_enum import EnumField
from app.Resource.all_resources import TimeEnum


class WorkerSchema(Schema):
    id = fields.String(required=False)
    name = fields.String(required=True, error_messages={"required": "Bad request - name is required"})
    surname = fields.String(required=True, error_messages={"required": "Bad request - surname is required"})
    position = fields.String(required=True, error_messages={"required": "Bad request - position is required"})


class ShiftSchema(Schema):
    id = fields.String(required=False)
    worker_id = fields.String(required=True, error_messages={"required": "Bad request - worker_id is required"})
    shift_time = EnumField(TimeEnum, by_value=True, required=True, error_messages={"required": "Bad request - shift time is required"})
    shift_date = fields.Date('%Y-%m-%d', required=True, error_messages={"required": "Bad request - shift date is required"})


class ShiftResultSchema(Schema):
    id = fields.String()
    worker = fields.Nested(WorkerSchema)
    shift_time = EnumField(TimeEnum, by_value=True)
    shift_date = fields.String()


worker_schema = WorkerSchema()
shift_schema = ShiftSchema()
shift_result_schema = ShiftResultSchema()
