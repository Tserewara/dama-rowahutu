from flask import request, jsonify, session
from flask.views import MethodView

from src.articles.domain.entities import exceptions
from src.articles.services import credential_service, unit_of_work


class LoginAPI(MethodView):

    @staticmethod
    def post():

        try:

            username = credential_service.login(
                username=request.json['username'],
                password=request.json['password'],
                uow=unit_of_work.SqlAlchemyUnitOfWork()
            )

            session['username'] = username

            return jsonify({'message': 'Logging successful!'}), 200

        except exceptions.CredentialValueError as e:

            return jsonify({'message': f'{str(e)}'}), 401
