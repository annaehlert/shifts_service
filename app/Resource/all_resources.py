from app import db
from app.db_functions import terminate_request
import uuid
import enum
import json
import datetime


class Worker(db.Model):
    __tablename__ = 'workers'
    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(128), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    shifts = db.relationship('Shift', backref='worker')

    @classmethod
    def get_worker_by_uuid(cls, id):
        try:
            return cls.query. \
                filter_by(id=id). \
                one()
        except Exception as e:
            terminate_request(404, str(e))

    @classmethod
    def get_worker_by_name_and_surname(cls, name, surname):
        try:
            return cls.query. \
                filter_by(name=name). \
                filter_by(surname=surname). \
                first()
        except Exception as e:
            terminate_request(404, str(e))

    @classmethod
    def get_all_workers(cls):
        try:
            return cls.query.filter_by().all()
        except Exception as e:
            terminate_request(404, str(e))


class TimeEnum(enum.Enum):
    time_00_08 = "time_00_08"
    time_08_16 = "time_08_16"
    time_16_24 = "time_16_24"

    def __str__(self):
        return self.value


class Shift(db.Model):
    __tablename__ = "shifts"
    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    shift_time = db.Column(db.Enum(TimeEnum), nullable=False)
    shift_date = db.Column(db.String)
    worker_id = db.Column(db.String, db.ForeignKey('workers.id'), nullable=False)

    @classmethod
    def get_shift_by_uuid(cls, id):
        try:
            return cls.query. \
                filter_by(id=id). \
                first()
        except Exception as e:
            terminate_request(404, str(e))

    @classmethod
    def get_shifts_by_worker_id(cls, worker_id):
        try:
            return cls.query. \
                filter_by(worker_id=worker_id). \
                all()
        except Exception as e:
            terminate_request(404, str(e))

    @classmethod
    def get_all_shifts(cls):
        try:
            return cls.query. \
                filter_by(). \
                all()
        except Exception as e:
            terminate_request(404, str(e))

    @classmethod
    def get_shift_by_worker_id_shift_time_shift_date(cls, worker_id, shift_time, shift_date):
        try:
            return cls.query. \
                filter_by(worker_id=worker_id). \
                filter_by(shift_time=shift_time). \
                filter_by(shift_date=shift_date). \
                first()
        except Exception:
            return None

    @classmethod
    def get_shift_by_worker_id_shift_date(cls, worker_id, shift_date):
        try:
            return cls.query. \
                filter_by(worker_id=worker_id). \
                filter_by(shift_date=shift_date). \
                first()
        except Exception:
            return None
