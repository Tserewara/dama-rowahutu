from flask import Blueprint


rest_api = Blueprint('rest_api',
                     __name__,
                     url_prefix='/api')


from .routes import rest_api
