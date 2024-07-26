URL='http://localhost:56733/'
import requests
from faker import Faker
import pytest
fake=Faker()

@pytest.fixture()
def register():
    body = {"username": fake.email(), "password": fake.password()}
    response_register = requests.post(url=f'{URL}/register', json=body)
    assert response_register.status_code == 201
    assert response_register.json()['message'] == 'User created successfully.'
    assert response_register.json()['uuid']
    return body