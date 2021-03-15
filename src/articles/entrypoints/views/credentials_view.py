from flask import request, jsonify
from flask.views import MethodView

from src.articles.domain.entities import exceptions
from src.articles.services import credential_service, unit_of_work


class CredentialsAPI(MethodView):

    @staticmethod
    def post():
        try:
            credential_service.add_credential(
                username=request.json['username'],
                password=request.json['password'],
                uow=unit_of_work.SqlAlchemyUnitOfWork()
            )
            return jsonify({"message": f"Credential created for user "
                                       f"{request.json['username']}"}), 201

        except exceptions.PasswordStrengthError as e:
            return jsonify(message=str(e)), 400
