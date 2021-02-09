from flask import Flask

from src.articles.entrypoints.rest import ArticlesAPI
from src.articles.entrypoints.routes import register_routes


def create_app():
    app = Flask(__name__)

    from src.articles.presentation.blog import articles_bp as articles

    app.register_blueprint(articles)

    app = register_routes(app)

    return app



