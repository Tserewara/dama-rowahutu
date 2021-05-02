from . import blog, views

blog.add_url_rule('/', view_func=views.home)
blog.add_url_rule('/artigos', view_func=views.get_articles)
blog.add_url_rule('/login', view_func=views.login)
blog.add_url_rule('/secret', view_func=views.secret)
blog.add_url_rule('/editor', view_func=views.editor)
