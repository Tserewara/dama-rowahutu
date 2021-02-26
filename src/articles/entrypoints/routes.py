from src.articles.entrypoints.rest import ArticlesAPI, CredentialsAPI, LoginAPI


def register_routes(app):

    app.add_url_rule('/articles', view_func=ArticlesAPI.as_view('articles'))

    app.add_url_rule('/credentials',
                     view_func=CredentialsAPI.as_view('credentials'))

    app.add_url_rule('/login', view_func=LoginAPI.as_view('login'))

    return app
