from src.articles.adapters import repository
from src.articles.domain import model
from src.articles.services import services


class FakeRepository(repository.AbstractRepository):
    def __init__(self):
        self._articles = []

    def add(self, article):
        self._articles.append(article)

    def list(self):
        return self._articles


class FakeSession:
    committed = False

    def commit(self):
        self.committed = True


def test_service_adds_an_article():
    article = model.Article(
        title='An article',
        description='A great description',
        content='This is a useful article',
        tags=[model.Tag('verbos')],
        category=model.Category.GUIDE
    )

    repo = FakeRepository()

    article_title = services.add_article(article, repo, FakeSession())

    assert article_title == 'An article'
