import pytest

from src.articles.domain.entities import exceptions
from src.articles.services import article_service
from tests.unit.test_services.fakes import FakeUnitOfWork


def test_service_adds_an_article():
    article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    article_title = article_service.add_article(**article, uow=uow)

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

    with pytest.raises(exceptions.DuplicateTitle,
                       match="Can't create article. Title duplicate."):
        article_service.add_article(**article, uow=uow)
        article_service.add_article(**article, uow=uow)


def test_raises_error_for_category_not_found_when_adding_article():
    article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 5,
        'tags': ['verbos'],
    }

    with pytest.raises(exceptions.CategoryNotFound,
                       match='Category not found'):
        uow = FakeUnitOfWork()
        article_service.add_article(**article, uow=uow)
