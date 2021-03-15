import pytest
import requests

from src.articles import config


@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_201_and_creates_credential(postgres_session):
    url = config.get_api_url()

    _credential = {
        "username": "tserewara",
        "password": "Password@1"
    }

    r = requests.post(f'{url}/credentials', json=_credential)

    assert r.status_code == 201
    assert r.json()['message'] == f'Credential created for user ' \
                                  f'{_credential["username"]}'


@pytest.mark.usefixtures('restart_api')
def test_unhappy_path_returns_400_and_error_dict(postgres_session):
    url = config.get_api_url()

    _credential = {
        "username": "tserewara",
        "password": "password"
    }

    r = requests.post(f'{url}/credentials', json=_credential)

    assert r.status_code == 400
    assert r.json()['message'] == 'A strong password should contain at least' \
                                  ' 8 characters, 1 digit, 1 symbol, 1' \
                                  ' uppercase letter, and 1 lowercase letter'
