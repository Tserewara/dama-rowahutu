from datetime import datetime
from typing import List

from src.articles.domain.entities.category import Category
from src.articles.domain.entities.tag import Tag


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
