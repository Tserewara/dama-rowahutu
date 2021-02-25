from typing import Union

from src.articles.domain.entities import credential
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

    return f'Credential created for {username}'


def list_credentials(uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        all_credentials = uow.credentials.list()

    return all_credentials


def get_credential_by_username(
        username: str,
        uow: unit_of_work.AbstractUnitOfWork
) -> Union[credential.Credential, None]:
    with uow:

        try:
            return next(a_credential for a_credential in
                        list_credentials(
                            uow) if a_credential.username == username)
        except StopIteration:
            return None
