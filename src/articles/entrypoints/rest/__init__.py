from flask import request, jsonify
from flask.views import MethodView

from src.articles.domain import model
from src.articles.services import services, unit_of_work


class ArticlesAPI(MethodView):

    @staticmethod
    def post():
        try:
            article = services.add_article(
                title=request.json['title'],
                description=request.json['description'],
                content=request.json['content'],
                tags=request.json['tags'],
                category_id=request.json['category_id'],
                uow=unit_of_work.SqlAlchemyUnitOfWork()
            )

            return jsonify(message=article), 201

        except (model.CategoryNotFound, model.DuplicateTitle) as e:
            return jsonify(message=str(e)), 404
