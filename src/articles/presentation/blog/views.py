from flask import render_template

from src.articles.services import unit_of_work


def get_articles():
    with unit_of_work.SqlAlchemyUnitOfWork() as uow:
        articles = uow.articles.list()

        return render_template('home.html', articles=articles), 200
