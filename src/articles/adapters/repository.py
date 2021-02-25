import abc
from typing import List

from src.articles.domain.entities import credential, article


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, entity):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_one_by(self, value: str):
        raise NotImplementedError


class SqlAlchemyRepositoryArticles(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, _article: article.Article):
        self.session.add(_article)

    def list(self):
        return self.session.query(article.Article).all()

    def get_one_by(self, value: str):
        pass


class SqlAlchemyRepositoryTags(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, _article: article.Article):
        self.session.add(_article)

    def list(self):
        return self.session.query(article.Article).all()

    def get_one_by(self, value: str):
        pass


class SqlAlchemyRepositoryCredentials(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, _credential: credential.AbstractCredential):
        self.session.add(_credential)

    def list(self) -> List[credential.Credential]:
        return self.session.query(credential.Credential).all()

    def get_one_by(self, username: str) -> credential.Credential:
        return self.session.query(credential.Credential).filter_by(
            username=username).first()
