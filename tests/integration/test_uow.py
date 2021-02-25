from src.articles.domain.entities import category, article, tag
from src.articles.services import unit_of_work


def test_uow_can_add_an_article(session_factory):

    _article = article.Article(
        title='An article',
        description='A great description',
        content='This is a useful article',
        tags=[tag.Tag('verbos')],
        category=category.Category.GUIDE
    )

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)

    with uow:
        uow.articles.add(_article)
        uow.commit()

    session = session_factory()

    retrieved_article = session.query(article.Article).first()

    assert retrieved_article.title == 'An article'
