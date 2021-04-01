from flask import Blueprint

blog = Blueprint('articles_bp',
                 __name__,
                 template_folder='templates')

from .routes import blog
