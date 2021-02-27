from src.articles.domain.entities import credential, exceptions
from src.articles.services import unit_of_work


def add_credential(
        username: str,
        password: str,
        uow: unit_of_work.AbstractUnitOfWork) -> str:
    with uow:
        new_credential = credential.Credential.factory(
            username=username,
            password=password
        )

        uow.credentials.add(new_credential)
        uow.commit()

    return f'Credential created for {username}'


def authenticate(
        username: str,
        password: str,
        uow: unit_of_work.AbstractUnitOfWork) -> str:

    with uow:

        _credential = uow.credentials.get_one_by(username)

        if not _credential:
            raise exceptions.CredentialValueError(
                'Invalid credential. Username not found.')

        if not _credential.verify_password(password):
            raise exceptions.CredentialValueError(
                'Password wrong!')

        return _credential.username
