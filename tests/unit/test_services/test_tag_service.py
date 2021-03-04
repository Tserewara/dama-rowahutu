from src.articles.domain.entities import tag
from src.articles.services import tag_service
from tests.unit.test_services.fakes import FakeUnitOfWork


def test_can_add_tag():
    uow = FakeUnitOfWork()

    tag_service.add_tag('verbos', uow)

    assert uow.tags.list().pop() == 'verbos'


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
