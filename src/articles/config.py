import os


def get_postgres_uri():
    host = os.environ.get('POSTGRES_HOST', 'localhost')
    port = 5432
    password = os.environ.get('POSTGRES_PASSWORD', 'xavante')
    user, db_name = 'postgres', 'damarowahutu-blog'
    return f'postgresql://{user}:{password}@{host}:{port}/{db_name}'


def get_api_url():
    host = os.environ.get('API_HOST', 'localhost')
    port = 5000 if host == 'localhost' else 80
    return f'http://{host}:{port}'
