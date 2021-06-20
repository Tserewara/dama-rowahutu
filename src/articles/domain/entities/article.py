import re
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
        self.url = self.build_friendly_url()

    def build_friendly_url(self):
        clean_title = self._remove_special_characters()
        split_title = clean_title.lower().split()
        self.url = '-'.join(e for e in split_title if e.isalnum())
        return self.url

    def _remove_special_characters(self):
        return re.sub(r"\W+|_", " ", self.title)

