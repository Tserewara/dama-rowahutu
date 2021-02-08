from src.articles.adapters import repository
from src.articles.domain import model


def test_repository_can_add_an_article(session):

    article = model.Article(
        title='An article',
        description='A great description',
        content='This is a useful article',
        tags=[model.Tag('verbos')],
        category=model.Category.GUIDE
    )

    repo = repository.SqlAlchemyRepositoryArticles(session)

    repo.add(article)
    session.commit()

    assert session.query(model.Article).first() == article