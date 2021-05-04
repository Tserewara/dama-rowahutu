from src.articles.entrypoints.rest_api.views.articles_view import ArticlesAPI
from .views.authentication_view import AuthenticationAPI
from .views.credentials_view import CredentialsAPI
from .views.tags_view import TagsAPI

from ..rest_api import rest_api

articles_view = ArticlesAPI.as_view('articles')

rest_api.add_url_rule('/articles', view_func=articles_view)
rest_api.add_url_rule('/articles/<string:title>', view_func=articles_view,
                      methods=['GET', 'PUT', 'DELETE'])

rest_api.add_url_rule('/credentials',
                      view_func=CredentialsAPI.as_view('credentials'))

rest_api.add_url_rule('/login',
                      view_func=AuthenticationAPI.as_view('login'))

rest_api.add_url_rule('/tags', view_func=TagsAPI.as_view('tags'))
