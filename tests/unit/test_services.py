from src.articles.adapters import repository
from src.articles.domain import model
from src.articles.services import services, unit_of_work


class FakeRepositoryArticles(repository.AbstractRepository):
    def __init__(self):
        self._articles = []

    def add(self, article):
        self._articles.append(article)

    def list(self):
        return self._articles


class FakeRepositoryTags(repository.AbstractRepository):
    def __init__(self):
        self._tags = []

    def add(self, article):
        self._tags.append(article)

    def list(self):
        return self._tags


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self):
        self.articles = FakeRepositoryArticles()
        self.tags = FakeRepositoryTags()
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


def test_can_add_tag():
    uow = FakeUnitOfWork()

    services.add_tag('verbos', uow)

    assert uow.tags.list().pop() == 'verbos'


def test_list_tags():
    uow = FakeUnitOfWork()

    services.add_tag('verbos', uow)
    services.add_tag('vocabulário', uow)

    assert services.list_tags(uow) == ['verbos', 'vocabulário']