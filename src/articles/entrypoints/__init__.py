from flask import Flask

from src.articles.entrypoints.routes import register_routes
from src.articles.adapters.start_db import wait_for_postgres_to_come_up


def create_app():
    app = Flask(__name__)

    from src.articles.presentation.blog import articles_bp as articles

    app.register_blueprint(articles)

    app = register_routes(app)

    wait_for_postgres_to_come_up()

    return app
