import pytest

from src.articles.domain.entities import exceptions
from src.articles.services import credential_service
from tests.unit.test_services.fakes import FakeUnitOfWork


def test_service_can_create_credential():
    uow = FakeUnitOfWork()

    result = credential_service.add_credential(
        'Tserewara',
        'password1',
        uow
    )

    assert result == 'Credential created for Tserewara'


def test_service_can_update_password():
    uow = FakeUnitOfWork()

    credential_service.add_credential(
        'Tserewara',
        'password1',
        uow
    )

    result = credential_service.update_credential(
        'Tserewara',
        new_password='password10',
        uow=uow
    )

    assert result == 'Credential updated for user Tserewara'
    assert credential_service.authenticate('Tserewara', 'password10', uow)


def test_service_can_update_username():
    uow = FakeUnitOfWork()

    _credential = ('Tserewara', 'password1')

    credential_service.add_credential(
        _credential[0],
        _credential[1],
        uow
    )

    result = credential_service.update_credential(
        'Tserewara',
        new_username='Tsere',
        uow=uow
    )

    assert result == 'Credential updated for user Tserewara'
    assert credential_service.authenticate('Tsere', 'password1', uow)


def test_can_delete_credential():
    uow = FakeUnitOfWork()

    _credential = ('Tserewara', 'password1')

    credential_service.add_credential(
        _credential[0],
        _credential[1],
        uow
    )

    credential_service.delete_credential('Tserewara', uow)

    assert uow.credentials.list() == []


def test_raises_credential_value_error_when_deleting_credential_non_existent():
    uow = FakeUnitOfWork()

    with pytest.raises(exceptions.CredentialValueError,
                       match='Credential not found'):
        credential_service.delete_credential('Tserewara', uow)


class TestLogin:

    def test_returns_true_when_logging_is_successful(self):
        uow = FakeUnitOfWork()

        credential_service.add_credential('Tserewara', 'password1', uow)

        username = credential_service.authenticate(
            'Tserewara',
            'password1',
            uow
        )

        assert username == 'Tserewara'

    def test_raises_exception_when_logging_with_invalid_username(self):
        uow = FakeUnitOfWork()

        _credential = ('Tserewara', 'password1')

        credential_service.add_credential(_credential[0], _credential[1], uow)

        with pytest.raises(exceptions.CredentialValueError,
                           match='Invalid credential. Username not found'):
            credential_service.authenticate('John', 'password', uow)
