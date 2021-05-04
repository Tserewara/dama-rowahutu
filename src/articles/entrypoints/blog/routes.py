from . import blog, views

urls_views = [
    ('/', views.home),
    ('/artigos', views.get_articles),
    ('/login', views.login),
    ('/secret', views.secret),
    ('/editor', views.editor),
]

for url, view in urls_views:
    blog.add_url_rule(url, view_func=view)
