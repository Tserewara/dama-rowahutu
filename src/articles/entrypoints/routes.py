from src.articles.entrypoints import ArticlesAPI


def register_routes(app):

    app.add_url_rule('/articles', view_func=ArticlesAPI.as_view('articles'))

    return app
