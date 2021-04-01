from flask import Blueprint

blog = Blueprint('blog',
                 __name__,
                 template_folder='templates',
                 static_folder='static_folder'
                 )

from .routes import blog
