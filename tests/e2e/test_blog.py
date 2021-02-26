import pytest
import requests

from src.articles import config
from tests.e2e.fake_authentication import authenticate


@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_home_page_and_200(postgres_session):
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

    fake_session.post(f'{url}/articles', json=article)

    r = fake_session.get(f'{url}/artigos')

    assert r.status_code == 200
    assert '<h1>Articles</h1>' in r.text
    assert f'<h1>{article["title"]}</h1>' in r.text
