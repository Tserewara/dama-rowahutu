from . import blog, views

urls_views = [
    ('/', views.home),
    ('/artigo/<string:title>', views.article),
    ('/login', views.login),
    ('/secret', views.secret),
    ('/editor', views.editor),
]

for url, view in urls_views:
    blog.add_url_rule(url, view_func=view)
