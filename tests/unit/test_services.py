import pytest

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


class FakeRepositoryCredentials(repository.AbstractRepository):
    def __init__(self):
        self._credentials = []

    def add(self, article):
        self._credentials.append(article)

    def list(self):
        return self._credentials


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self):
        self.articles = FakeRepositoryArticles()
        self.tags = FakeRepositoryTags()
        self.credentials = FakeRepositoryCredentials()
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
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    article_title = services.add_article(**article, uow=uow)

    assert article_title == 'An article'


def test_raises_error_for_duplicate_title():
    article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    with pytest.raises(model.DuplicateTitle,
                       match="Can't create article. Title duplicate."):
        services.add_article(**article, uow=uow)
        services.add_article(**article, uow=uow)


def test_raises_error_when_category_is_not_found():
    article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 5,
        'tags': ['verbos'],
    }

    with pytest.raises(model.CategoryNotFound,
                       match='Category not found'):
        uow = FakeUnitOfWork()
        services.add_article(**article, uow=uow)


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


def test_gets_valid_tags():
    uow = FakeUnitOfWork()

    taglist = ['verbos', 'vocabulário', 'pronomes']

    for tag in taglist:
        services.add_tag(tag, uow)

    tags_to_check = taglist + ['invalid 1', 'invalid 2']

    valid_tags = services.get_valid_tags_by_name(tags_to_check, uow)

    assert valid_tags == taglist


def test_returns_empty_list_when_tags_is_none():
    uow = FakeUnitOfWork()

    valid_tags = services.get_valid_tags_by_name(None, uow)

    assert valid_tags == []


class TestCredentialService:

    def test_service_can_create_credential(self):
        uow = FakeUnitOfWork()

        my_credential = ('Tserewara', 'password')

        result = services.add_credential(
            my_credential[0],
            my_credential[1],
            uow
        )

        assert result == f'Credential created for {my_credential[0]}'

    def test_lists_all_credentials(self):
        uow = FakeUnitOfWork()

        my_credentials = [
            ('User_A', 'password1'),
            ('User_B', 'password2'),
            ('User_C', 'password3'),
        ]

        for item in my_credentials:
            services.add_credential(item[0], item[1], uow)

        assert len(services.list_credentials(uow)) == 3

    def test_returns_credential_by_username(self):
        uow = FakeUnitOfWork()

        my_credential = ('Tserewara', 'password')

        services.add_credential(my_credential[0], my_credential[1], uow)

        result_credential = services.get_credential_by_username(
            'Tserewara', uow)

        assert result_credential.username == my_credential[0]

    def test_returns_true_when_credential_is_equal(self):
        uow = FakeUnitOfWork()

        my_credential = ('Tserewara', 'password')

        services.add_credential(my_credential[0], my_credential[1], uow)

        result_credential = services.get_credential_by_username(
            'Tserewara', uow)

        assert result_credential.verify_password('password')
