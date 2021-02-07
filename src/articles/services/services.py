from src.articles.adapters import repository
from src.articles.domain import model
from src.articles.services import unit_of_work


def add_article(
        title: str,
        description: str,
        content: str,
        tags: list,
        uow: unit_of_work.AbstractUnitOfWork) -> str:

    with uow:
        article = model.Article(title, description, content, tags)
        uow.articles.add(article)
        uow.commit()

    return title
