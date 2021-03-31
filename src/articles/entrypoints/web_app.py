from src.articles.adapters import orm
from src.articles.entrypoints.app_factory import create_app

app = create_app()
orm.start_mappers()

if __name__ == '__main__':
    app.run(debug=True)
