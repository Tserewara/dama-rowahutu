from src.articles.adapters import repository
from src.articles.services import unit_of_work


class FakeRepositoryArticles(repository.AbstractRepository):
    def __init__(self):
        self._articles = []

    def add(self, article):
        self._articles.append(article)

    def list(self):
        return self._articles

    def get(self, value: str):
        for item in self.list():
            if item.url == value:
                return item

    def delete(self, entity):
        self._articles.remove(entity)


class FakeRepositoryTags(repository.AbstractRepository):
    def __init__(self):
        self._tags = []

    def add(self, article):
        self._tags.append(article)

    def list(self):
        return self._tags

    def get(self, value: str):
        for item in self.list():
            if item.name == value:
                return item

    def delete(self, entity):
        self._tags.remove(entity)


class FakeRepositoryCredentials(repository.AbstractRepository):
    def __init__(self):
        self._credentials = []

    def add(self, article):
        self._credentials.append(article)

    def list(self):
        return self._credentials

    def get(self, value: str):
        for item in self.list():
            if item.username == value:
                return item

    def delete(self, entity):
        self._credentials.remove(entity)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self):
        self.articles = FakeRepositoryArticles()
        self.tags = FakeRepositoryTags()
        self.credentials = FakeRepositoryCredentials()
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass
