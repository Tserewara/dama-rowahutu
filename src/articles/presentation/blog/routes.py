from . import articles_bp
from . import views

articles_bp.add_url_rule('/artigos', view_func=views.get_articles)
