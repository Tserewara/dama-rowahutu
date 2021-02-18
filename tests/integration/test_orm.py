from src.articles.domain import model


def tag_factory():
    return [
        model.Tag('verbos'),
        model.Tag('vocabulario'),
        model.Tag('subtantivo'),
        model.Tag('gramatica')
    ]


def test_orm_can_save_article(session):
    article = model.Article(
        title='An article',
        description='A great description',
        content='This is a useful article',
        tags=tag_factory(),
        category=model.Category.GUIDE
    )

    session.add(article)
    session.commit()

    assert session.query(model.Article).first().title == 'An article'


def test_orm_deletes_a_tag_used_in_article(session):
    article = model.Article(
        title='An article',
        description='A great description',
        content='This is a useful article',
        tags=tag_factory(),
        category=model.Category.GUIDE
    )

    session.add(article)
    session.commit()

    tag = session.query(model.Tag).first()

    session.delete(tag)
    session.commit()

    assert len(session.query(model.Article).first().tags) == 3


def test_orm_saves_date_of_article(session):
    article = model.Article(
        title='An article',
        description='A great description',
        content='This is a useful article',
        tags=tag_factory(),
        category=model.Category.GUIDE
    )

    session.add(article)
    session.commit()

    assert session.query(model.Article).first().created_on
