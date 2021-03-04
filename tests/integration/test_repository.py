from src.articles.adapters import repository
from src.articles.domain.entities import credential, category, article, tag


class TestRepositoryArticles:

    def test_can_add_an_article(self, session):
        _article = article.Article(
            title='An article',
            description='A great description',
            content='This is a useful article',
            tags=[tag.Tag('verbos')],
            category=category.Category.GUIDE
        )

        repo = repository.SqlAlchemyRepositoryArticles(session)

        repo.add(_article)
        session.commit()

        assert session.query(article.Article).first() == _article

    def test_gets_article_by_title(self, session):
        _article = article.Article(
            title='An article',
            description='A great description',
            content='This is a useful article',
            tags=[tag.Tag('verbos')],
            category=category.Category.GUIDE
        )

        repo = repository.SqlAlchemyRepositoryArticles(session)

        repo.add(_article)
        session.commit()

        assert _article == repo.get(value='An article')


class TestRepositoryCredential:

    def test_can_add_credential(self, session):
        _credential = credential.Credential.factory(
            username='tserewara',
            password='password',
        )

        repo = repository.SqlAlchemyRepositoryCredentials(session)

        repo.add(_credential)
        session.commit()

        assert session.query(credential.Credential).first() == _credential
