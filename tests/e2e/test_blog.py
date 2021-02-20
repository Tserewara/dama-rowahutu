import pytest
import requests

from src.articles import config


# @pytest.mark.skip('temp skip')
@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_home_page_and_200(postgres_session):
    url = config.get_api_url()

    article = {
        "title": "An article",
        "description": "A remarkable description",
        "content": "Some very useful content",
        "tags": [],
        "category_id": 1
    }

    requests.post(f'{url}/articles', json=article)

    r = requests.get(f'{url}/artigos')

    assert r.status_code == 200
    assert '<h1>Articles</h1>' in r.text
    assert f'<h1>{article["title"]}</h1>' in r.text
