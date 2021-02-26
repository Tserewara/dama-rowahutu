from flask import request, jsonify
from flask.views import MethodView

from src.articles.domain.entities import exceptions
from src.articles.services import article_service, unit_of_work


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
