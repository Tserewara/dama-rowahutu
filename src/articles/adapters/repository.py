import abc
from typing import List

from src.articles.domain.entities import credential, article, tag


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, entity):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, value: str):
        raise NotImplementedError

    def delete(self, entity: article.Article):
        raise NotImplementedError


class SqlAlchemyRepositoryArticles(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, _article: article.Article):
        self.session.add(_article)

    def list(self):
        return self.session.query(article.Article).all()

    def get(self, value: str):
        return self.session.query(article.Article).filter_by(
            url=value).first()

    def delete(self, entity: article.Article):
        self.session.delete(entity)


class SqlAlchemyRepositoryTags(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, _tag: tag.Tag):
        self.session.add(_tag)

    def list(self):
        return self.session.query(tag.Tag).all()

    def get(self, value: str):
        pass

    def delete(self, entity: tag.Tag):
        self.session.delete(entity)


class SqlAlchemyRepositoryCredentials(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, _credential: credential.AbstractCredential):
        self.session.add(_credential)

    def list(self) -> List[credential.Credential]:
        return self.session.query(credential.Credential).all()

    def get(self, username: str) -> credential.Credential:
        return self.session.query(credential.Credential).filter_by(
            username=username).first()

    def delete(self, entity: credential.Credential):
        self.session.delete(entity)
