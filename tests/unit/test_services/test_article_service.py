import pytest

from src.articles.domain.entities import article, exceptions, tag, category
from src.articles.services import article_service
from tests.unit.test_services.fakes import FakeUnitOfWork


def create_tags(uow):
    _tags = [tag.Tag('verbos'), tag.Tag('substantivos'), tag.Tag('dicas')]

    for _tag in _tags:
        uow.tags.add(_tag)
    uow.commit()


def test_returns_true_when_title_is_duplicate():
    uow = FakeUnitOfWork()

    article_1 = article.Article(
        title='An article',
        description='A great description',
        content='This is a useful article',
        category=category.Category.CULTURE,
        tags=[tag.Tag('verbos'), tag.Tag('substantivos')])

    article_2 = article.Article(
        title='Another article',
        description='A great description',
        content='This is a useful article',
        category=category.Category.CULTURE,
        tags=[tag.Tag('verbos'), tag.Tag('substantivos')])

    uow.articles.add(article_1)
    uow.articles.add(article_2)
    uow.commit()

    assert article_service.title_is_duplicate(title='An article', uow=uow)
    assert article_service.title_is_duplicate(title='Another article', uow=uow)


def test_returns_false_when_title_is_not_duplicate():
    uow = FakeUnitOfWork()

    article_1 = article.Article(
        title='An article',
        description='A great description',
        content='This is a useful article',
        category=category.Category.CULTURE,
        tags=[tag.Tag('verbos'), tag.Tag('substantivos')])

    uow.articles.add(article_1)

    uow.commit()

    assert article_service.title_is_duplicate(title='A new article',
                                              uow=uow) is False


def test_returns_false_when_passing_article_to_exclude_from_comparison():
    uow = FakeUnitOfWork()

    article_1 = article.Article(
        title='An article',
        description='A great description',
        content='This is a useful article',
        category=category.Category.CULTURE,
        tags=[tag.Tag('verbos'), tag.Tag('substantivos')])

    article_2 = article.Article(
        title='Another article',
        description='A great description',
        content='This is a useful article',
        category=category.Category.CULTURE,
        tags=[tag.Tag('verbos'), tag.Tag('substantivos')])

    uow.articles.add(article_1)
    uow.articles.add(article_2)
    uow.commit()

    assert article_service.title_is_duplicate(title='An article',
                                              article_to_update=article_1,
                                              uow=uow) is False


def test_service_adds_an_article():
    uow = FakeUnitOfWork()

    create_tags(uow)

    _article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    article_title = article_service.add_article(**_article, uow=uow)

    result = uow.articles.get('An article')

    assert article_title == 'An article'
    assert result.tags == [tag.Tag('verbos'), tag.Tag('substantivos')]


def test_raises_error_for_duplicate_title():
    _article = {
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
        article_service.add_article(**_article, uow=uow)
        article_service.add_article(**_article, uow=uow)


def test_raises_error_for_category_not_found_when_adding_article():
    _article = {
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

        article_service.add_article(**_article, uow=uow)


def test_can_update_article_title():
    _article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    create_tags(uow)

    article_service.add_article(**_article, uow=uow)

    article_service.update_article(
        article_title='An article',
        title='A new article',
        uow=uow)

    updated = uow.articles.get(value='A new article')

    assert updated.title == 'A new article'


def test_can_update_article_description():
    _article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    article_service.add_article(**_article, uow=uow)

    create_tags(uow)

    article_service.update_article(
        article_title='An article',
        description='Simple description',
        uow=uow)

    updated = uow.articles.get(value='An article')

    assert updated.description == 'Simple description'


def test_can_update_many_article_attributes_at_once():
    _article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    create_tags(uow)

    article_service.add_article(**_article, uow=uow)

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
    _article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    create_tags(uow)

    article_service.add_article(**_article, uow=uow)

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
    _article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    article_service.add_article(**_article, uow=uow)

    with pytest.raises(exceptions.ArticleNotFound, match='Article not found.'):
        article_service.update_article(
            article_title='Another article',
            title='A new article',
            uow=uow
        )


def test_raises_attribute_error_when_updating_non_existent_attribute():
    _article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    article_service.add_article(**_article, uow=uow)

    with pytest.raises(AttributeError):
        article_service.update_article(
            article_title='An article',
            uow=uow,
            wrong_attribute='Another article'
        )


def test_raises_duplicate_title_error_when_updating_and_title_exists():
    article_1 = {
        'title': 'An article 1',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    article_2 = {
        'title': 'An article 2',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    article_service.add_article(**article_1, uow=uow)
    article_service.add_article(**article_2, uow=uow)

    with pytest.raises(exceptions.DuplicateTitle):
        article_service.update_article(
            article_title='An article 1',
            title='An article 2',
            uow=uow,
        )


def test_deletes_an_article():
    _article = {
        'title': 'An article',
        'description': 'A great description',
        'content': 'This is a useful article',
        'category_id': 1,
        'tags': ['verbos', 'substantivos'],
    }

    uow = FakeUnitOfWork()

    article_service.add_article(**_article, uow=uow)

    article_service.delete_article('an-article', uow)

    assert uow.articles.list() == []


def test_raises_article_not_found_error_when_deleting_non_existent_article():
    uow = FakeUnitOfWork()

    with pytest.raises(exceptions.ArticleNotFound):
        article_service.delete_article('An article', uow)
