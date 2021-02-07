from src.articles.domain import model
from src.articles.services import unit_of_work


def test_uow_can_add_an_article(session_factory):

    article = model.Article(
        title='An article',
        description='A great description',
        content='This is a useful article',
        tags=[model.Tag('verbos')],
        category=model.Category.GUIDE
    )

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)

    with uow:
        uow.articles.add(article)
        uow.commit()

    session = session_factory()

    retrieved_article = session.query(model.Article).first()

    assert retrieved_article.title == 'An article'