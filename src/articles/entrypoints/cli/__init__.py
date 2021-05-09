import click
from flask import Blueprint

from src.articles.domain.entities import exceptions
from src.articles.services import unit_of_work, credential_service

cli = Blueprint('cli', __name__)


@cli.cli.command('create_credential')
@click.argument('username')
@click.argument('password')
def create(username, password):

    uow = unit_of_work.SqlAlchemyUnitOfWork()

    try:
        result = credential_service.add_credential(
            username=username,
            password=password,
            uow=uow
        )
        print(result)

    except exceptions.PasswordStrengthError as error:
        print(str(error))

