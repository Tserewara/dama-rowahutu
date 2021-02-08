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





