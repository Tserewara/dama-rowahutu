from src.articles.domain.entities import article, exceptions
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
        article_title: str, uow: unit_of_work.AbstractUnitOfWork, **kwargs):
    with uow:

        _article = uow.articles.get(value=article_title)

        if not _article:
            raise exceptions.ArticleNotFound('Article not found.')

        for attribute in kwargs:
            if not hasattr(_article, attribute):
                raise AttributeError(f'Article has no attribute {attribute}')

        if 'title' in kwargs:
            setattr(_article, 'title', kwargs['title'])

        if 'description' in kwargs:
            setattr(_article, 'description', kwargs['description'])

        if 'content' in kwargs:
            setattr(_article, 'content', kwargs['content'])

        if 'category' in kwargs:
            setattr(_article, 'category', kwargs['category'])

        if 'tags' in kwargs:
            setattr(_article, 'tags', tag_service.get_valid_tags_by_name(
                kwargs['tags'], uow))

        uow.commit()

    return article_title


def title_is_duplicate(
        title: str,
        uow: unit_of_work.AbstractUnitOfWork):
    with uow:

        try:
            return next(_article.title for _article in uow.articles.list() if
                        _article.title == title) is not None
        except StopIteration:
            return False


def _update_article_tags(_article, _tags, uow):
    valid_tags = tag_service.get_valid_tags_by_name(_tags, uow)

    setattr(_article, 'tags', valid_tags)
