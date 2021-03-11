from src.articles.domain.entities import credential, category, article, tag


def tag_factory():
    return [
        tag.Tag('verbos'),
        tag.Tag('vocabulario'),
        tag.Tag('subtantivo'),
        tag.Tag('gramatica')
    ]


def test_orm_can_save_article(session):

    _article = article.Article(
        title='An article',
        description='A great description',
        content='This is a useful article',
        tags=tag_factory(),
        category=category.Category.GUIDE
    )

    session.add(_article)
    session.commit()

    assert session.query(article.Article).first().title == 'An article'


def test_orm_deletes_a_tag_used_in_article(session):

    _article = article.Article(
        title='An article',
        description='A great description',
        content='This is a useful article',
        tags=tag_factory(),
        category=category.Category.GUIDE
    )

    session.add(_article)
    session.commit()

    _tag = session.query(tag.Tag).first()

    session.delete(_tag)
    session.commit()

    assert len(session.query(article.Article).first().tags) == 3


def test_orm_saves_date_of_article(session):

    _article = article.Article(
        title='An article',
        description='A great description',
        content='This is a useful article',
        tags=tag_factory(),
        category=category.Category.GUIDE
    )

    session.add(_article)
    session.commit()

    assert session.query(article.Article).first().created_on


def test_can_save_credential(session):

    _credential = credential.Credential.factory(
        username='tserewara',
        password='password1'
    )

    # _credential.set_password('password1')

    session.add(_credential)
    session.commit()

    assert session.query(credential.Credential).first() == _credential
