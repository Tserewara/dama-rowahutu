from src.articles.adapters import repository
from src.articles.domain import model
from src.articles.services import services, unit_of_work


class FakeRepository(repository.AbstractRepository):
    def __init__(self):
        self._articles = []

    def add(self, article):
        self._articles.append(article)

    def list(self):
        return self._articles


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self):
        self.articles = FakeRepository()
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass


def test_service_adds_an_article():
    article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': [model.Tag('verbos')],

    }

    uow = FakeUnitOfWork()

    article_title = services.add_article(**article, uow=uow)

    assert article_title == 'An article'


def test_category_exists():
    assert services.get_category(1)
    assert not services.get_category(999)
