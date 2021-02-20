import time

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError, ProgrammingError
from sqlalchemy.orm import sessionmaker

from src.articles import config
from src.articles.adapters.orm import metadata, articles


def tables_exist():
    session = sessionmaker(bind=create_engine(config.get_postgres_uri()))()
    try:
        session.execute(f'SELECT 1 FROM {articles.name};')
        return True
    except ProgrammingError:
        return False


def create_tables():
    if not tables_exist():
        metadata.create_all(create_engine(config.get_postgres_uri()))


def wait_for_postgres_to_come_up():
    engine = create_engine(config.get_postgres_uri())

    while True:
        try:
            if engine.connect():
                create_tables()
                print("POSTGRES IS UP")
                break
        except OperationalError:
            time.sleep(0.5)
            print("POSTGRES NEVER CAME UP...")
