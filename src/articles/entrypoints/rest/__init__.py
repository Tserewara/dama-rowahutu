from flask import request, jsonify
from flask.views import MethodView

from src.articles.domain.entities import exceptions
from src.articles.services import (article_service, credential_service,
                                   unit_of_work)


class ArticlesAPI(MethodView):

    @staticmethod
    def post():
        try:
            article = article_service.add_article(
                title=request.json['title'],
                description=request.json['description'],
                content=request.json['content'],
                tags=request.json['tags'],
                category_id=request.json['category_id'],
                uow=unit_of_work.SqlAlchemyUnitOfWork()
            )

            return jsonify(message=article), 201

        except (exceptions.CategoryNotFound, exceptions.DuplicateTitle) as e:
            return jsonify(message=str(e)), 404


class CredentialsAPI(MethodView):

    @staticmethod
    def post():
        credential_service.add_credential(
            username=request.json['username'],
            password=request.json['password'],
            uow=unit_of_work.SqlAlchemyUnitOfWork()
        )
        return jsonify({"message": f"Credential created for user "
                                   f"{request.json['username']}"}), 201


class LoginAPI(MethodView):

    @staticmethod
    def post():

        try:

            result = credential_service.login(
                username=request.json['username'],
                password=request.json['password'],
                uow=unit_of_work.SqlAlchemyUnitOfWork()
            )

            return jsonify({'message': result}), 200

        except exceptions.CredentialValueError as e:

            return jsonify({'message': f'{str(e)}'}), 401
