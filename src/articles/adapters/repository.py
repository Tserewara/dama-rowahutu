import abc

from src.articles.domain import model


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, entity):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self):
        raise NotImplementedError


class SqlAlchemyRepositoryArticles(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, article: model.Article):
        self.session.add(article)

    def list(self):
        return self.session.query(model.Article).all()


class SqlAlchemyRepositoryTags(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, article: model.Article):
        self.session.add(article)

    def list(self):
        return self.session.query(model.Article).all()
