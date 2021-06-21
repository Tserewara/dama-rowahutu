import pytest
import requests

from src.articles import config
from tests.e2e.fake_authentication import authenticate


@pytest.mark.usefixtures('restart_api')
def test_happy_path_post_returns_201_and_article_title(postgres_session):
    url = config.get_api_url()

    fake_session = requests.Session()

    authenticate(fake_session)

    article = {
        "title": "An article",
        "description": "A remarkable description",
        "content": "Some very useful content",
        "tags": [],
        "category_id": 1
    }

    r = fake_session.post(f'{url}/api/articles', json=article)

    assert r.status_code == 201
    assert r.json()['message'] == 'An article'


@pytest.mark.usefixtures('restart_api')
def test_unhappy_path_post_returns_404_and_error_message(postgres_session):
    url = config.get_api_url()

    fake_session = requests.Session()

    authenticate(fake_session)

    article = {
        "title": "An article",
        "description": "A remarkable description",
        "content": "Some very useful content",
        "tags": [],
        "category_id": 1
    }

    fake_session.post(f'{url}/api/articles', json=article)
    r = fake_session.post(f'{url}/api/articles', json=article)

    assert r.status_code == 404
    assert r.json()['message'] == 'Can\'t create article. Title duplicate.'


@pytest.mark.usefixtures('restart_api')
def test_happy_path_delete_returns_200_and_message(postgres_session):
    url = config.get_api_url()

    fake_session = requests.Session()

    authenticate(fake_session)

    article = {
        "title": "An article",
        "description": "A remarkable description",
        "content": "Some very useful content",
        "tags": [],
        "category_id": 1
    }

    fake_session.post(f'{url}/api/articles', json=article)

    r = fake_session.delete(f'{url}/api/articles/an-article')
    assert r.status_code == 200
    assert r.json()['message'] == 'Article deleted'


@pytest.mark.usefixtures('restart_api')
def test_unhappy_path_delete_returns_404_and_message(postgres_session):
    url = config.get_api_url()

    fake_session = requests.Session()

    authenticate(fake_session)

    r = fake_session.delete(f'{url}/api/articles/an-article')
    assert r.status_code == 404
    assert r.json()['message'] == 'Article not found.'
