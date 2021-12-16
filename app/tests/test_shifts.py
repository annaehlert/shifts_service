import json
from app import application


def test_shifts():
    ''' correct parameters '''
    ''' creation of new user '''
    params_worker = {'name': 'Joe',
                     'surname': 'Doe',
                     'position': 'Manager'}
    response = application.test_client().post('/maintenance', data=json.dumps(params_worker))
    response_data = json.loads(response.data)
    params = {'worker_id': response_data["id"],
              'shift_time': 'time_00_08',
              'shift_date': '2021-09-10'}
    response = application.test_client().post('/management', data=json.dumps(params))
    response_data = json.loads(response.data)
    response_2 = application.test_client().get('/management')
    response_3 = application.test_client().get(f'/management?worker_id={response_data.get("worker").get("id")}')
    changed_params = {'shift_time': 'time_08_16',
                      'shift_date': '2021-10-10'}
    response_4 = application.test_client().patch(f'/management/{response_data["id"]}', data=json.dumps(changed_params))
    response_5 = application.test_client().delete(f'/management/{response_data["id"]}')
    assert response.status_code == 200
    assert response_2.status_code == 200
    assert response_3.status_code == 200
    assert response_4.status_code == 200
    assert response_5.status_code == 200
    ''' wrong params '''
    params_wrong = {'worker_id': response_data["id"],
                    'shift_date': '2021-09-10'}
    wrong_response = application.test_client().post('/management', data=json.dumps(params_wrong))
    wrong_response_2 = application.test_client().get(f'/management?worker_id={12}')
    assert wrong_response.status_code == 400
    assert wrong_response_2.status_code == 404
    response_6 = application.test_client().delete(f'/user/{response_data.get("worker").get("id")}')
    assert response_6.status_code == 200
