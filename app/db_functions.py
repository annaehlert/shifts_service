from flask import abort

from app import application, db
import json


def create_database():
    try:
        db.create_all()
        return {'status': 'OK'}, 200
    except Exception as e:
        return {'error': e}, 500


def terminate_request(code, message):
    data = {'message': message}
    response = application.response_class(response=json.dumps(data),
                                          status=code,
                                          mimetype='application/json')
    abort(response)


def commit_or_abort(error_message=None, code=500):
    try:
        db.session.commit()
        return {'status': 'OK'}, 200
    except Exception as e:
        db.session.rollback()
        terminate_request(code, error_message or e)


