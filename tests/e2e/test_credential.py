import pytest
import requests

from src.articles import config


@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_201_and_creates_credential(postgres_session):
    url = config.get_api_url()

    _credential = {
        "username": "tserewara",
        "password": "pass!word"
    }

    r = requests.post(f'{url}/credentials', json=_credential)

    assert r.status_code == 201
    assert r.json()['message'] == f'Credential created for user ' \
                                  f'{_credential["username"]}'
