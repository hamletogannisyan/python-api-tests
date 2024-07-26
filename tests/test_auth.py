URL='http://localhost:56733/'
import requests
from faker import Faker
import pytest
fake=Faker()

class TestAuth:
    def test_auth_with_valid_data(self, register):
        response_auth = requests.post(url=f'{URL}/auth', json=register)
        assert response_auth.status_code == 200
