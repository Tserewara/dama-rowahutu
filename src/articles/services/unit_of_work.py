import abc

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.articles import config
from src.articles.adapters import repository


class AbstractUnitOfWork(abc.ABC):
    articles: repository.AbstractRepository
    tags: repository.AbstractRepository

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(config.get_postgres_uri()),
)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.articles = repository.SqlAlchemyRepositoryArticles(self.session)
        self.articles = repository.SqlAlchemyRepositoryTags(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        self.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
