from sqlalchemy import (MetaData, Table, Column, Integer, String, ForeignKey,
                        Enum, DateTime, func, Boolean)
from sqlalchemy.orm import mapper, relationship

from src.articles.domain.entities import credential, category, article, tag

metadata = MetaData()

articles = Table('articles', metadata,
                 Column('id', Integer, primary_key=True, autoincrement=True),
                 Column('title', String, index=True, unique=True,
                        nullable=False),
                 Column('description', String, nullable=False),
                 Column('content', String, nullable=False),
                 Column('category', Enum(category.Category)),
                 Column('created_on', DateTime(timezone=True),
                        server_default=func.now()),
                 )

tags = Table('tags', metadata,
             Column('id', Integer, primary_key=True, autoincrement=True),
             Column('name', String, nullable=False)
             )

article_tags = Table('article_tags', metadata,
                     Column('id', Integer, primary_key=True,
                            autoincrement=True),
                     Column('article_id', Integer,
                            ForeignKey('articles.id')),
                     Column('tag_id', Integer,
                            ForeignKey('tags.id'))
                     )

credentials = Table('credentials', metadata,
                    Column('id', Integer, primary_key=True,
                           autoincrement=True),
                    Column('username', String, index=True,
                           unique=True, nullable=False),
                    Column('password', String, nullable=False),
                    Column('active', Boolean)
                    )


def start_mappers():
    tags_mapper = mapper(tag.Tag, tags)

    mapper(article.Article, articles, properties={
        'tags': relationship(
            tags_mapper,
            secondary=article_tags,
            backref='tags'
        )
    })

    mapper(credential.Credential, credentials)
