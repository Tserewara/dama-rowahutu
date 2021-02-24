from typing import Union, List

from src.articles.domain import model, credential
from src.articles.services import unit_of_work


def add_article(
        title: str,
        description: str,
        content: str,
        category_id: id,
        uow: unit_of_work.AbstractUnitOfWork,
        tags: list = None) -> str:
    with uow:

        category = get_category(category_id)

        if title_is_duplicate(title, uow):
            raise model.DuplicateTitle('Can\'t create article. Title '
                                       'duplicate.')

        if not category:
            raise model.CategoryNotFound('Category not found')

        tags = get_valid_tags_by_name(tags, uow)

        article = model.Article(
            title,
            description,
            content,
            tags,
            category
        )

        uow.articles.add(article)
        uow.commit()

    return title


def title_is_duplicate(title: str, uow: unit_of_work.AbstractUnitOfWork):
    with uow:

        try:
            return next(article.title for article in uow.articles.list() if
                        article.title == title) is not None
        except StopIteration:
            return False


def get_category(category: int) -> Union[model.Category, None]:
    try:
        return model.Category(category)
    except ValueError:
        return None


def add_tag(tag_name: str, uow: unit_of_work.AbstractUnitOfWork) -> str:
    with uow:
        uow.tags.add(tag_name)

    return tag_name


def list_tags(uow: unit_of_work.AbstractUnitOfWork) -> List[model.Tag]:
    with uow:
        tags = uow.tags.list()

    return tags


def get_valid_tags_by_name(tags: Union[list, None], uow) -> List[model.Tag]:
    if not tags:
        return []

    return [tag for tag in tags if tag in list_tags(uow)]


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
            return next(a_credential for a_credential in list_credentials(
                uow) if a_credential.username == username)
        except StopIteration:
            return None
