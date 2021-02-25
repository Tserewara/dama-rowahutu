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

        if title_is_duplicate(title, uow):
            raise exceptions.DuplicateTitle('Can\'t create article. Title '
                                            'duplicate.')

        if not category:
            raise exceptions.CategoryNotFound('Category not found')

        tags = tag_service.get_valid_tags_by_name(tags, uow)

        _article = article.Article(
            title,
            description,
            content,
            tags,
            category
        )

        uow.articles.add(_article)
        uow.commit()

    return title


def title_is_duplicate(
        title: str,
        uow: unit_of_work.AbstractUnitOfWork):
    with uow:

        try:
            return next(_article.title for _article in uow.articles.list() if
                        _article.title == title) is not None
        except StopIteration:
            return False
