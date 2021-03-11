from src.articles.domain.entities import credential, exceptions
from src.articles.services import unit_of_work


def add_credential(
        username: str,
        password: str,
        uow: unit_of_work.AbstractUnitOfWork) -> str:

    with uow:

        new_credential = credential.Credential.factory(
            username=username,
        )

        new_credential.set_password(password)

        uow.credentials.add(new_credential)
        uow.commit()

    return f'Credential created for {username}'


def update_credential(
        username: str,
        uow: unit_of_work.AbstractUnitOfWork,
        new_username: str = None,
        new_password: str = None,
) -> str:

    _credential = get_credential(username, uow)

    def update_username():

        if uow.credentials.get(new_username):
            raise exceptions.CredentialValueError('Username is already taken.')
        _credential.username = new_username

    def update_password():
        _credential.set_password(new_password)

    if new_username:
        update_username()

    if new_password:
        update_password()

    uow.commit()

    return f'Credential updated for user {username}'


def get_credential(username: str, uow: unit_of_work.AbstractUnitOfWork):

    _credential = uow.credentials.get(value=username)

    if not _credential:
        raise exceptions.CredentialValueError('Credential not found')

    return _credential


def delete_credential(username: str, uow: unit_of_work.AbstractUnitOfWork):

    with uow:

        _credential = get_credential(username, uow)

        uow.credentials.delete(_credential)

        uow.commit()


def authenticate(
        username: str,
        password: str,
        uow: unit_of_work.AbstractUnitOfWork) -> str:
    with uow:

        _credential = uow.credentials.get(username)

        if not _credential:
            raise exceptions.CredentialValueError(
                'Invalid credential. Username not found.')

        if not _credential.verify_password(password):
            raise exceptions.CredentialValueError(
                'Password wrong!')

        return _credential.username
