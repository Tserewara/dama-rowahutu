import abc

from src.articles.domain.entities import credential, article


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

    def add(self, _article: article.Article):
        self.session.add(_article)

    def list(self):
        return self.session.query(article.Article).all()


class SqlAlchemyRepositoryTags(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, _article: article.Article):
        self.session.add(_article)

    def list(self):
        return self.session.query(article.Article).all()


class SqlAlchemyRepositoryCredentials(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, _credential: credential.AbstractCredential):
        self.session.add(_credential)

    def list(self):
        return self.session.query(credential.Credential).all()
