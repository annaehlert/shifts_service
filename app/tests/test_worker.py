import json
from app import application


def test_worker():
    ''' correct parameters '''
    params = {'name': 'Joe',
              'surname': 'Doe',
              'position': 'Manager'}
    response = application.test_client().post('/maintenance', data=json.dumps(params))
    response_data = json.loads(response.data)
    response_2 = application.test_client().get('/user')
    response_3 = application.test_client().get(f'/user/{response_data["id"]}')
    changed_params = {'name': 'Karen',
                      'surname': 'Dwight',
                      'position': 'Director'}
    response_4 = application.test_client().patch(f'/maintenance/{response_data["id"]}', data=json.dumps(changed_params))
    response_5 = application.test_client().delete(f'/user/{response_data["id"]}')
    assert response.status_code == 200
    assert response_2.status_code == 200
    assert response_3.status_code == 200
    assert response_4.status_code == 200
    assert response_5.status_code == 200

    ''' wrong params '''
    wrong_params = {'name': 12,
                    'surname': 'Doe',
                    'position': 'Manager'}
    wrong_params_2 = {'name': 12,
                      'position': 'Manager'}
    response_wrong = application.test_client().post('/maintenance', data=json.dumps(wrong_params))
    response_wrong_2 = application.test_client().post('/maintenance', data=json.dumps(wrong_params_2))

    assert response_wrong.status_code == 400
    assert response_wrong_2.status_code == 400
