from flask import Flask, request, jsonify

from src.articles.adapters import orm
from src.articles.domain import model
from src.articles.services import services, unit_of_work

app = Flask(__name__)
orm.start_mappers()


@app.route('/articles', methods=['POST'])
def articles():
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

    except model.CategoryNotFound as e:
        return jsonify(message=str(e)), 404


if __name__ == '__main__':
    app.run(debug=True)
