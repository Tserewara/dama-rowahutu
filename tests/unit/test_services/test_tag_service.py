import pytest

from src.articles.domain.entities import tag, exceptions
from src.articles.services import tag_service
from tests.unit.test_services.fakes import FakeUnitOfWork


def test_service_can_add_tag():
    uow = FakeUnitOfWork()

    tag_name = tag_service.add_tag('verbos', uow)

    assert tag_name == 'verbos'


def test_service_raises_error_for_duplicate_tag():
    uow = FakeUnitOfWork()

    with pytest.raises(exceptions.DuplicateTag):
        tag_service.add_tag('verbos', uow)
        tag_service.add_tag('verbos', uow)


def test_gets_valid_tags():
    uow = FakeUnitOfWork()

    tag_list = [tag.Tag('dicas'), tag.Tag('verbos'), tag.Tag('substantivos')]

    for _tag in tag_list:
        uow.tags.add(_tag)

    tags_to_check = ['dicas', 'verbos', 'substantivos', 'invalid1', 'invalid2']

    valid_tags = tag_service.get_valid_tags_by_name(tags_to_check, uow)

    assert valid_tags == tag_list


def test_returns_empty_list_when_tags_is_none():
    uow = FakeUnitOfWork()

    valid_tags = tag_service.get_valid_tags_by_name(None, uow)

    assert valid_tags == []


def test_service_can_delete_tag():
    uow = FakeUnitOfWork()

    tag_list = [tag.Tag('dicas'), tag.Tag('verbos'), tag.Tag('substantivos')]

    for _tag in tag_list:
        uow.tags.add(_tag)

    assert len(uow.tags.list()) == 3

    tag_service.delete_tag('dicas', uow)

    assert len(uow.tags.list()) == 2


def test_raises_tag_not_found_error_when_deleting_non_existent_tag():
    uow = FakeUnitOfWork()

    tag_list = [tag.Tag('dicas'), tag.Tag('verbos'), tag.Tag('substantivos')]

    for _tag in tag_list:
        uow.tags.add(_tag)

    assert len(uow.tags.list()) == 3

    with pytest.raises(exceptions.TagNotFound,
                       match='Tag not found'):

        tag_service.delete_tag('adjetivos', uow)


def test_service_can_update_tag():
    uow = FakeUnitOfWork()

    tag_list = [tag.Tag('dicas'), tag.Tag('verbos'), tag.Tag('substantivos')]

    for _tag in tag_list:
        uow.tags.add(_tag)

    assert len(uow.tags.list()) == 3

    tag_service.update_tag(tag_name='dicas', new_name='sugestões', uow=uow)

    assert uow.tags.get('sugestões')
