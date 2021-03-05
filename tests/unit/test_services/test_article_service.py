import pytest

from src.articles.domain.entities import exceptions, tag
from src.articles.services import article_service
from tests.unit.test_services.fakes import FakeUnitOfWork


def create_tags(uow):
    _tags = [tag.Tag('verbos'), tag.Tag('substantivos'), tag.Tag('dicas')]

    for _tag in _tags:
        uow.tags.add(_tag)
    uow.commit()


def test_service_adds_an_article():
    uow = FakeUnitOfWork()

    create_tags(uow)

    article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    article_title = article_service.add_article(**article, uow=uow)

    _article = uow.articles.get('An article')

    assert article_title == 'An article'
    assert _article.tags == [tag.Tag('verbos'), tag.Tag('substantivos')]


def test_raises_error_for_duplicate_title():
    article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    create_tags(uow)

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
                       match='Category not found.'):
        uow = FakeUnitOfWork()

        create_tags(uow)

        article_service.add_article(**article, uow=uow)


def test_can_update_article_title():
    article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    create_tags(uow)

    article_service.add_article(**article, uow=uow)

    article_service.update_article(
        article_title='An article',
        title='A new article',
        uow=uow)

    updated = uow.articles.get(value='A new article')

    assert updated.title == 'A new article'


def test_can_update_article_description():
    article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    article_service.add_article(**article, uow=uow)

    create_tags(uow)

    article_service.update_article(
        article_title='An article',
        description='Simple description',
        uow=uow)

    updated = uow.articles.get(value='An article')

    assert updated.description == 'Simple description'


def test_can_update_many_article_attributes_at_once():
    article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    create_tags(uow)

    article_service.add_article(**article, uow=uow)

    _article = uow.articles.get('An article')

    assert _article.tags == [tag.Tag('verbos'), tag.Tag('substantivos')]

    article_service.update_article(
        article_title='An article',
        description='A new description',
        content='A new content',
        category=2,
        tags=['dicas'],
        uow=uow)

    updated = uow.articles.get('An article')

    assert updated.description == 'A new description'
    assert updated.content == 'A new content'
    assert updated.category == 2
    assert updated.tags == [tag.Tag('dicas')]


def test_can_update_tags_of_article():
    article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    create_tags(uow)

    article_service.add_article(**article, uow=uow)

    _article = uow.articles.get(value='An article')

    article_service.update_attribute(
        _article,
        attribute='tags',
        _kwargs={'tags': ['verbos']},
        uow=uow
    )

    updated = uow.articles.get(value='An article')
    assert updated.tags == [tag.Tag('verbos')]


def test_raises_article_not_found_entity_when_updating():
    article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    article_service.add_article(**article, uow=uow)

    with pytest.raises(exceptions.ArticleNotFound, match='Article not found.'):
        article_service.update_article(
            article_title='Another article',
            title='A new article',
            uow=uow
        )


def test_raises_attribute_error_when_updating_non_existent_attribute():
    article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    article_service.add_article(**article, uow=uow)

    with pytest.raises(AttributeError):
        article_service.update_article(
            article_title='An article',
            uow=uow,
            wrong_attribute='Another article'
        )
