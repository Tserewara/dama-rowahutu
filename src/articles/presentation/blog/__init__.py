from flask import Blueprint

articles_bp = Blueprint('articles_bp',
                        __name__,
                        template_folder='templates')

from .routes import articles_bp
