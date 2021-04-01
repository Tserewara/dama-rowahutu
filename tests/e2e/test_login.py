import pytest
import requests

from src.articles import config


@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_201_and_success_message_when_logging_succeeds(
        postgres_session):
    url = config.get_api_url()

    _credential = {
        "username": "tserewara",
        "password": "Password1"
    }

    requests.post(f'{url}/api/credentials', json=_credential)

    r = requests.post(f'{url}/api/login', json=_credential)

    assert r.status_code == 200
    assert r.json()['message'] == 'Logging successful!'


@pytest.mark.usefixtures('restart_api')
def test_unhappy_path_returns_401_and_fail_message_when_username_is_wrong(
        postgres_session):
    url = config.get_api_url()

    _credential = {
        "username": "tserewara",
        "password": "Password1"
    }

    fail_credential = {
        "username": "john",
        "password": "pass!word"
    }

    requests.post(f'{url}/api/credentials', json=_credential)

    r = requests.post(f'{url}/api/login', json=fail_credential)

    assert r.status_code == 401
    assert r.json()['message'] == 'Invalid credential. Username not found.'


@pytest.mark.usefixtures('restart_api')
def test_unhappy_path_returns_401_and_fail_message_when_password_is_wrong(
        postgres_session):

    url = config.get_api_url()

    _credential = {
        "username": "tserewara",
        "password": "Password1"
    }

    fail_credential = {
        "username": "tserewara",
        "password": "pass!word1"
    }

    requests.post(f'{url}/api/credentials', json=_credential)

    r = requests.post(f'{url}/api/login', json=fail_credential)

    assert r.status_code == 401
    assert r.json()['message'] == 'Password wrong!'
