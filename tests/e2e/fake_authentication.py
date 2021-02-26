from src.articles import config


def authenticate(fake_session):
    url = config.get_api_url()

    _credential = {
        "username": "tserewara",
        "password": "pass!word"
    }

    fake_session.post(f'{url}/credentials', json=_credential)

    fake_session.post(f'{url}/login', json=_credential)
