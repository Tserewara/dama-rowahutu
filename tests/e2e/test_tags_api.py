import pytest
import requests

from src.articles import config
from tests.e2e.fake_authentication import authenticate


@pytest.mark.usefixtures('restart_api')
def test_happy_path_post_returns_201_and_tag_name(postgres_session):
    url = config.get_api_url()

    fake_session = requests.Session()

    authenticate(fake_session)

    tag = {'tag_name': 'verbos'}

    r = requests.post(f'{url}/api/tags', json=tag)

    assert r.status_code == 201
    assert r.json()['message'] == tag['tag_name']


@pytest.mark.usefixtures('restart_api')
def test_unhappy_path_post_returns_409_and_error_message(postgres_session):
    url = config.get_api_url()

    fake_session = requests.Session()

    authenticate(fake_session)

    tag = {'tag_name': 'verbos'}

    requests.post(f'{url}/api/tags', json=tag)
    r = requests.post(f'{url}/api/tags', json=tag)

    assert r.status_code == 409
    assert r.json()['message'] == f'Tag {tag["tag_name"]} is duplicate'
