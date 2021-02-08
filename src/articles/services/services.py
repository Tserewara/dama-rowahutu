from typing import Union, List

from src.articles.domain import model
from src.articles.services import unit_of_work


def add_article(
        title: str,
        description: str,
        content: str,
        tags: list,
        category_id: id,
        uow: unit_of_work.AbstractUnitOfWork) -> str:
    with uow:
        category = get_category(category_id)

        if not category:
            raise model.CategoryNotFound('Category not found')

        article = model.Article(
            title,
            description,
            content,
            tags,
            category
        )
        uow.articles.add(article)
        uow.commit()

    return title


def get_category(category: int) -> Union[model.Category, None]:
    try:
        return model.Category(category)
    except ValueError:
        return None


def add_tag(tag_name: str, uow: unit_of_work.AbstractUnitOfWork) -> str:
    with uow:
        uow.tags.add(tag_name)

    return tag_name


def list_tags(uow: unit_of_work.AbstractUnitOfWork) -> List[model.Tag]:
    with uow:
        tags = uow.tags.list()

    return tags
