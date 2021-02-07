from src.articles.adapters import repository
from src.articles.domain import model


def add_article(
        article: model.Article,
        repo: repository.AbstractRepository,
        session) -> str:

    repo.add(article)
    session.commit()

    return article.title
