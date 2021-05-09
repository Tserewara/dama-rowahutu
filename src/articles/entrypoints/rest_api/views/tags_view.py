from flask import request, jsonify
from flask.views import MethodView

from src.articles.domain.entities import exceptions
from src.articles.entrypoints.authentication import authentication_required
from src.articles.services import tag_service, unit_of_work


class TagsAPI(MethodView):
    decorators = [authentication_required]

    @staticmethod
    def post():

        try:
            tag_name = tag_service.add_tag(
                tag_name=request.json['tag_name'].lower(),
                uow=unit_of_work.SqlAlchemyUnitOfWork()
            )

            return jsonify(message=tag_name), 201

        except exceptions.DuplicateTag as e:
            return jsonify(message=str(e)), 409
