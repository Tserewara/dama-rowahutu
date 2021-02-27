from .views.authentication_view import AuthenticationAPI
from .views.credentials_view import CredentialsAPI
from .views.articles_view import ArticlesAPI


def register_routes(app):

    app.add_url_rule('/articles', view_func=ArticlesAPI.as_view('articles'))

    app.add_url_rule('/credentials',
                     view_func=CredentialsAPI.as_view('credentials'))

    app.add_url_rule('/login', view_func=AuthenticationAPI.as_view('login'))

    return app
