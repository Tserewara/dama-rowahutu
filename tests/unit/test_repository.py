from src.articles.adapters import repository
from src.articles.domain import model, credential


class TestRepositoryArticles:

    def test_can_add_an_article(self, session):
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


class TestRepositoryCredential:

    def test_can_add_credential(self, session):

        my_credential = credential.Credential.factory(
            username='tserewara',
            password='password',
        )

        repo = repository.SqlAlchemyRepositoryCredentials(session)

        repo.add(my_credential)
        session.commit()

        assert session.query(credential.Credential).first() == my_credential
