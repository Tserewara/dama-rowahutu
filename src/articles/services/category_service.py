from typing import Union

from src.articles.domain.entities import category


def get_category(_category: int) -> Union[category.Category, None]:
    try:
        return category.Category(_category)
    except ValueError:
        return None
