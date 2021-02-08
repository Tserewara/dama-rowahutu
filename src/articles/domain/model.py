from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List


class Category(Enum):
    GUIDE = 1
    CULTURE = 2
    EXERCISES = 3


class CategoryNotFound(Exception):
    pass


@dataclass
class Tag:
    name: str


class Article:

    def __init__(self,
                 title: str,
                 description: str,
                 content: str,
                 tags: List[Tag],
                 category: Category = Category.GUIDE):
        self.title = title
        self.description = description
        self.content = content
        self.tags = tags
        self.category = category
        self.created_on = datetime.now()
