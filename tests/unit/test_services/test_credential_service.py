import pytest

from src.articles.domain.entities import exceptions
from src.articles.services import credential_service
from tests.unit.test_services.fakes import FakeUnitOfWork


def test_service_can_create_credential():
    uow = FakeUnitOfWork()

    _credential = ('Tserewara', 'password')

    result = credential_service.add_credential(
        _credential[0],
        _credential[1],
        uow
    )

    assert result == f'Credential created for {_credential[0]}'


class TestLogin:

    def test_returns_true_when_logging_is_successful(self):
        uow = FakeUnitOfWork()

        _credential = ('Tserewara', 'password')

        credential_service.add_credential(_credential[0], _credential[1], uow)

        username = credential_service.authenticate(
            'Tserewara',
            'password',
            uow)

        assert username == 'Tserewara'

    def test_raises_exception_when_logging_with_invalid_username(self):
        uow = FakeUnitOfWork()

        _credential = ('Tserewara', 'password')

        credential_service.add_credential(_credential[0], _credential[1], uow)

        with pytest.raises(exceptions.CredentialValueError,
                           match='Invalid credential. Username not found'):

            credential_service.authenticate('John', 'password', uow)
