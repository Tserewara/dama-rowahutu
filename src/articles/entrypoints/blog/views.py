from flask import render_template

from src.articles.entrypoints.authentication import authentication_required
from src.articles.services import unit_of_work


def get_articles():
    with unit_of_work.SqlAlchemyUnitOfWork() as uow:
        articles = uow.articles.list()

        return render_template('home.html', articles=articles), 200


def login():
    return render_template('login.html'), 200


@authentication_required
def secret():
    return render_template('secret.html'), 200
