from src.articles import config


def authenticate(fake_session):
    url = config.get_api_url()

    _credential = {
        "username": "tserewara",
        "password": "Password1"
    }

    fake_session.post(f'{url}/api/credentials', json=_credential)

    fake_session.post(f'{url}/api/login', json=_credential)
