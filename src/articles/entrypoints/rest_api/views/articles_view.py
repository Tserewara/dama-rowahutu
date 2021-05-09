from flask import request, jsonify
from flask.views import MethodView

from src.articles.domain.entities import exceptions

from src.articles.entrypoints.authentication import authentication_required
from src.articles.services import article_service, unit_of_work


class ArticlesAPI(MethodView):
    decorators = [authentication_required]

    @staticmethod
    def post():
        try:

            article = article_service.add_article(
                title=request.json['title'],
                description=request.json['description'],
                content=request.json['content'],
                tags=request.json['tags'],
                category_id=int(request.json['category_id']),
                uow=unit_of_work.SqlAlchemyUnitOfWork()
            )

            return jsonify(message=article), 201

        except (exceptions.CategoryNotFound, exceptions.DuplicateTitle) as e:
            return jsonify(message=str(e)), 404

    @staticmethod
    def delete(title):
        try:
            article_service.delete_article(
                article_title=title,
                uow=unit_of_work.SqlAlchemyUnitOfWork()
            )

            return jsonify({'message': 'Article deleted'}), 200

        except exceptions.ArticleNotFound as e:
            return jsonify(message=str(e)), 404
