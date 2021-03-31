from . import blog, views

blog.add_url_rule('/artigos', view_func=views.get_articles)
