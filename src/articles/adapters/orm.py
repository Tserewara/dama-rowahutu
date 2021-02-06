from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, \
    Enum
from sqlalchemy.orm import mapper, relationship

from src.articles.domain import model

metadata = MetaData()

articles = Table('articles', metadata,
                 Column('id', Integer, primary_key=True, autoincrement=True),
                 Column('title', String, index=True, unique=True,
                        nullable=False),
                 Column('description', String, nullable=False),
                 Column('content', String, nullable=False),
                 Column('category', Enum(model.Category))
                 )

tags = Table('tags', metadata,
             Column('id', Integer, primary_key=True, autoincrement=True),
             Column('name', String, nullable=False)
             )

article_tags = Table('article_tags', metadata,
                     Column('id', Integer, primary_key=True,
                            autoincrement=True),
                     Column('article_id', Integer, ForeignKey('articles.id')),
                     Column('tag_id', Integer, ForeignKey('tags.id'))
                     )


def start_mappers():
    tags_mapper = mapper(model.Tag, tags)
    mapper(model.Article, articles, properties={
        'tags': relationship(
            tags_mapper,
            secondary=article_tags
        )
    })

