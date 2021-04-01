import os

from flask import Flask


from src.articles.adapters.start_db import wait_for_postgres_to_come_up


def create_app():
    app = Flask(__name__)

    app.secret_key = os.environ.get('SECRET_KEY', 'tserewara')

    from .rest_api import rest_api
    from .blog import blog

    app.register_blueprint(rest_api)
    app.register_blueprint(blog)

    wait_for_postgres_to_come_up()

    return app
