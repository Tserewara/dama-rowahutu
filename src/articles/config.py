import os


def get_postgres_uri():
    host = os.environ.get('DB_HOST', 'localhost')
    port = 5432 if host == 'localhost' else 54321
    password = os.environ.get('DB_PASSWORD', 'xavante')
    user, db_name = 'postgres', 'damarowahutu'
    return f'postgresql://{user}:{password}@{host}:{port}/{db_name}'


def get_api_url():
    host = os.environ.get('API_HOST', 'localhost')
    port = 5000 if host == 'localhost' else 80
    return f'http://{host}:{port}'
