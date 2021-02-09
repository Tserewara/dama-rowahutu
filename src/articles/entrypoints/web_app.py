from src.articles.adapters import orm
from src.articles.entrypoints import create_app

app = create_app()
orm.start_mappers()

if __name__ == '__main__':
    app.run(debug=True)
