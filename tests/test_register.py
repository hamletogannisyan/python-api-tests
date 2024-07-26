URL='http://localhost:56733/'
import requests
from faker import Faker
import pytest
fake=Faker()

class TestRegister:
    def test_register_with_valid_data(self):
        body={"username": fake.email(), "password": fake.password()}
        response = requests.post(url=f'{URL}/register', json=body)
        assert response.status_code==201
        assert response.json()['message'] == 'User created successfully.'
        assert response.json()['uuid']

    @pytest.mark.skip(reason="it accepts invalid username")
    @pytest.mark.parametrize("username", ["test", 1234, False, "", {1,2,3}])
    def test_register_with_invalid_username(self, username):
        body = {"username": username, "password": fake.password()}
        response = requests.post(url=f'{URL}/register', json=body)
        assert response.status_code == 400

    @pytest.mark.skip(reason="it accepts invalid password")
    @pytest.mark.parametrize("password", ["1", 4, False, " ", {1,2,3}])
    def test_register_with_invalid_username(self, password):
        body = {"username": fake.email(), "password": password}
        response = requests.post(url=f'{URL}/register', json=body)
        assert response.status_code == 400

    def test_register_with_empty_username(self):
        body = {"username": None, "password": fake.password()}
        response = requests.post(url=f'{URL}/register', json=body)
        assert response.status_code == 400

    def test_register_with_empty_password(self):
        body = {"username": fake.email(), "password": None}
        response = requests.post(url=f'{URL}/register', json=body)
        assert response.status_code == 400

    def test_double_register_with_valid_data(self):
        body={"username": fake.email(), "password": fake.password()}
        response_1 = requests.post(url=f'{URL}/register', json=body)
        assert response_1.status_code==201
        response_2 = requests.post(url=f'{URL}/register', json=body)
        assert response_2.status_code == 400
        assert response_2.json()['message'] == 'A user with that username already exists'