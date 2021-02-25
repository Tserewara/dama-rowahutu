from src.articles.services import tag_service
from tests.unit.test_services.fakes import FakeUnitOfWork


def test_can_add_tag():
    uow = FakeUnitOfWork()

    tag_service.add_tag('verbos', uow)

    assert uow.tags.list().pop() == 'verbos'


def test_list_tags():
    uow = FakeUnitOfWork()

    tag_service.add_tag('verbos', uow)
    tag_service.add_tag('vocabulário', uow)

    assert tag_service.list_tags(uow) == ['verbos', 'vocabulário']


def test_gets_valid_tags():
    uow = FakeUnitOfWork()

    taglist = ['verbos', 'vocabulário', 'pronomes']

    for tag in taglist:
        tag_service.add_tag(tag, uow)

    tags_to_check = taglist + ['invalid 1', 'invalid 2']

    valid_tags = tag_service.get_valid_tags_by_name(tags_to_check, uow)

    assert valid_tags == taglist


def test_returns_empty_list_when_tags_is_none():
    uow = FakeUnitOfWork()

    valid_tags = tag_service.get_valid_tags_by_name(None, uow)

    assert valid_tags == []
