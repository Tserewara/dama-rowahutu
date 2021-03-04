from typing import List, Union

from src.articles.domain.entities import tag
from src.articles.services import unit_of_work


def add_tag(tag_name: str, uow: unit_of_work.AbstractUnitOfWork) -> str:
    with uow:
        uow.tags.add(tag_name)

    return tag_name


def get_valid_tags_by_name(
        _tags: Union[List[str], None],
        uow: unit_of_work.AbstractUnitOfWork
) -> List[tag.Tag]:

    return [_tag for _tag in uow.tags.list() if _tag.name in _tags]
