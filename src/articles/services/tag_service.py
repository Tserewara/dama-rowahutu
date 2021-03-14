from typing import List, Union

from src.articles.domain.entities import tag, exceptions
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


def delete_tag(tag_name: str, uow: unit_of_work.AbstractUnitOfWork) -> str:

    with uow:

        tag_to_delete = uow.tags.get(tag_name)

        if tag_to_delete is None:
            raise exceptions.TagNotFound('Tag not found')

        uow.tags.delete(tag_to_delete)

        uow.commit()

    return f'Tag {tag_name} deleted'


def update_tag(tag_name: str,
               new_name: str,
               uow: unit_of_work.AbstractUnitOfWork) -> str:
    with uow:

        tag_to_update = uow.tags.get(tag_name)

        if tag_name is None:
            raise exceptions.TagNotFound('Tag not found')

        tag_to_update.name = new_name

        uow.commit()

    return f'Tag {tag_name} updated to {new_name}'
