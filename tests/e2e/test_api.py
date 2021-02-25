import pytest
import requests

from src.articles import config


@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_201_and_article_title(postgres_session):
    url = config.get_api_url()

    article = {
        "title": "An article",
        "description": "A remarkable description",
        "content": "Some very useful content",
        "tags": [],
        "category_id": 1
    }

    r = requests.post(f'{url}/articles', json=article)

    assert r.status_code == 201
    assert r.json()['message'] == 'An article'


@pytest.mark.usefixtures('restart_api')
def test_unhappy_path_returns_201_and_article_title(postgres_session):
    url = config.get_api_url()

    article = {
        "title": "An article",
        "description": "A remarkable description",
        "content": "Some very useful content",
        "tags": [],
        "category_id": 1
    }

    requests.post(f'{url}/articles', json=article)
    r = requests.post(f'{url}/articles', json=article)

    assert r.status_code == 404
    assert r.json()['message'] == 'Can\'t create article. Title duplicate.'


@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_201_and_credential(postgres_session):
    url = config.get_api_url()

    _credential = {
        "username": "tserewara",
        "password": "pass!word"
    }

    r = requests.post(f'{url}/credentials', json=_credential)

    assert r.status_code == 201
    assert r.json()['message'] == f'Credential created for user ' \
                                  f'{_credential["username"]}'


@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_201_and_success_message_when_logging_succeeds(
        postgres_session):
    url = config.get_api_url()

    _credential = {
        "username": "tserewara",
        "password": "pass!word"
    }

    requests.post(f'{url}/credentials', json=_credential)

    r = requests.post(f'{url}/login', json=_credential)

    assert r.status_code == 200
    assert r.json()['message'] == 'Logging successful!'


@pytest.mark.usefixtures('restart_api')
def test_unhappy_path_returns_401_and_fail_message_when_username_is_wrong(
        postgres_session):
    url = config.get_api_url()

    _credential = {
        "username": "tserewara",
        "password": "pass!word"
    }

    fail_credential = {
        "username": "john",
        "password": "pass!word"
    }

    requests.post(f'{url}/credentials', json=_credential)

    r = requests.post(f'{url}/login', json=fail_credential)

    assert r.status_code == 401
    assert r.json()['message'] == 'Invalid credential. Username not found.'


@pytest.mark.usefixtures('restart_api')
def test_unhappy_path_returns_401_and_fail_message_when_password_is_wrong(
        postgres_session):
    url = config.get_api_url()

    _credential = {
        "username": "tserewara",
        "password": "pass!word"
    }

    fail_credential = {
        "username": "tserewara",
        "password": "pass!word1"
    }

    requests.post(f'{url}/credentials', json=_credential)

    r = requests.post(f'{url}/login', json=fail_credential)

    assert r.status_code == 401
    assert r.json()['message'] == 'Password wrong!'
