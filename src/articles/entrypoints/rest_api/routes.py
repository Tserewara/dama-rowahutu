from src.articles.entrypoints.rest_api.views.articles_view import ArticlesAPI
from .views.authentication_view import AuthenticationAPI
from .views.credentials_view import CredentialsAPI


def register_routes(blueprint):
    articles_view = ArticlesAPI.as_view('articles')

    blueprint.add_url_rule('/articles', view_func=articles_view)
    blueprint.add_url_rule('/articles/<string:title>', view_func=articles_view,
                           methods=['GET', 'PUT', 'DELETE'])

    blueprint.add_url_rule('/credentials',
                           view_func=CredentialsAPI.as_view('credentials'))

    blueprint.add_url_rule('/login',
                           view_func=AuthenticationAPI.as_view('login'))

    return blueprint
