from flask import render_template

from src.articles.domain.entities import category
from src.articles.entrypoints.authentication import authentication_required
from src.articles.services import unit_of_work


def home():
    with unit_of_work.SqlAlchemyUnitOfWork() as uow:
        articles = uow.articles.list()

        return render_template('home.html', articles=articles), 200


@authentication_required
def editor():
    categories = {
        'GUIA': category.Category.GUIDE,
        'CULTURA': category.Category.CULTURE,
        'EXERCÍCIOS': category.Category.EXERCISES
    }

    with unit_of_work.SqlAlchemyUnitOfWork() as uow:
        tags = uow.tags.list()
        serialized_tags = [tag.name for tag in tags]

    return render_template('editor.html',
                           categories=categories,
                           tags=serialized_tags
                           ), 200


def article(title):
    with unit_of_work.SqlAlchemyUnitOfWork() as uow:
        _article = uow.articles.get(title)

        if _article:
            return render_template('article.html', _article=_article)
    return '<h1>Página não encontrada</h1>', 404


def login():
    return render_template('login.html'), 200