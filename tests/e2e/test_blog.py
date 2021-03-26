import pytest
import requests

from src.articles import config
from tests.e2e.fake_authentication import authenticate


@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_home_page_and_200(
        postgres_session,
        selenium_web_driver):

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

    selenium_web_driver.get(f'{url}/artigos')

    page_title = selenium_web_driver.find_element_by_tag_name('h1').text
    post_title = selenium_web_driver.find_element_by_tag_name('h2').text
    description = selenium_web_driver.find_element_by_tag_name('p').text

    assert page_title == 'Articles'
    assert post_title == 'An article'
    assert description == 'A remarkable description'
