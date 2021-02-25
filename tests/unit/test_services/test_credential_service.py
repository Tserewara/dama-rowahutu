from src.articles.services import credential_service
from tests.unit.test_services.fakes import FakeUnitOfWork


def test_service_can_create_credential():
    uow = FakeUnitOfWork()

    my_credential = ('Tserewara', 'password')

    result = credential_service.add_credential(
        my_credential[0],
        my_credential[1],
        uow
    )

    assert result == f'Credential created for {my_credential[0]}'


def test_lists_all_credentials():
    uow = FakeUnitOfWork()

    my_credentials = [
        ('User_A', 'password1'),
        ('User_B', 'password2'),
        ('User_C', 'password3'),
    ]

    for item in my_credentials:
        credential_service.add_credential(item[0], item[1], uow)

    assert len(credential_service.list_credentials(uow)) == 3


def test_returns_credential_by_username():
    uow = FakeUnitOfWork()

    my_credential = ('Tserewara', 'password')

    credential_service.add_credential(my_credential[0], my_credential[1], uow)

    result_credential = credential_service.get_credential_by_username(
        'Tserewara', uow)

    assert result_credential.username == my_credential[0]


def test_returns_true_when_credential_is_equal():
    uow = FakeUnitOfWork()

    my_credential = ('Tserewara', 'password')

    credential_service.add_credential(my_credential[0], my_credential[1], uow)

    result_credential = credential_service.get_credential_by_username(
        'Tserewara', uow)

    assert result_credential.verify_password('password')
