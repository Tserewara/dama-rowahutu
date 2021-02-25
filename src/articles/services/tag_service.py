from typing import List, Union

from src.articles.domain.entities import tag
from src.articles.services import unit_of_work


def add_tag(tag_name: str, uow: unit_of_work.AbstractUnitOfWork) -> str:
    with uow:
        uow.tags.add(tag_name)

    return tag_name


def list_tags(uow: unit_of_work.AbstractUnitOfWork) -> List[tag.Tag]:
    with uow:
        tags = uow.tags.list()

    return tags


def get_valid_tags_by_name(
        tags: Union[list, None],
        uow: unit_of_work.AbstractUnitOfWork
) -> List[tag.Tag]:
    if not tags:
        return []

    return [_tag for _tag in tags if _tag in list_tags(uow)]
