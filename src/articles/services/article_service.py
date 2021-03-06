from src.articles.domain.entities import article, exceptions, tag
from src.articles.services import unit_of_work, category_service, tag_service


def add_article(
        title: str,
        description: str,
        content: str,
        category_id: id,
        uow: unit_of_work.AbstractUnitOfWork,
        tags: list = None) -> str:
    with uow:

        category = category_service.get_category(category_id)

        if not category:
            raise exceptions.CategoryNotFound('Category not found.')

        if title_is_duplicate(title, uow):
            raise exceptions.DuplicateTitle('Can\'t create article. Title '
                                            'duplicate.')

        _tags = tag_service.get_valid_tags_by_name(tags, uow) or []

        _article = article.Article(
            title,
            description,
            content,
            _tags,
            category
        )

        uow.articles.add(_article)
        uow.commit()

    return title


def update_article(
        article_title: str,
        uow: unit_of_work.AbstractUnitOfWork,
        **kwargs,
):
    with uow:

        _article = uow.articles.get(value=article_title)

        if not _article:
            raise exceptions.ArticleNotFound('Article not found.')

        for attribute in kwargs:
            update_attribute(_article, attribute, kwargs, uow)

        uow.commit()

    return article_title


def delete_article(article_title, uow: unit_of_work.AbstractUnitOfWork) -> str:
    with uow:
        _article = uow.articles.get(article_title)

        if not _article:
            raise exceptions.ArticleNotFound('Article not found.')

        uow.articles.delete(_article)

        uow.commit()

    return article_title


def title_is_duplicate(
        title: str,
        uow: unit_of_work.AbstractUnitOfWork,
        article_to_update: article.Article = None
):
    with uow:

        _articles = [_article for _article in uow.articles.list() if
                     _article != article_to_update]

        try:
            return next(_article for _article in _articles if
                        _article.title == title) is not None
        except StopIteration:
            return False


def update_attribute(
        _article,
        attribute,
        _kwargs,
        uow: unit_of_work.AbstractUnitOfWork
):
    if not hasattr(_article, attribute):
        raise AttributeError(f'Article has no attribute {attribute}')

    setattr(_article, attribute, _kwargs[attribute])

    if attribute == 'title':
        if title_is_duplicate(
                _kwargs['title'],
                article_to_update=_article,
                uow=uow):
            raise exceptions.DuplicateTitle('Title is duplicate')

        setattr(_article, attribute, _kwargs[attribute])

    if attribute == 'tags':
        _valid_tags = tag_service.get_valid_tags_by_name(
            _kwargs['tags'], uow)

        _article.tags = _valid_tags
