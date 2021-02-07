from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List


class Category(Enum):
    GUIDE = 1
    SHORT = 2


@dataclass
class Tag:
    name: str


class Article:

    def __init__(self,
                 title: str,
                 description: str,
                 content: str,
                 tags: List,
                 category: Category = Category.GUIDE):

        self.title = title
        self.description = description
        self.content = content
        self.tags = tags
        self.category = category
        self.created_on = datetime.now()
