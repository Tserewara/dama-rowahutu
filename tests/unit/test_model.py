from datetime import datetime

from src.articles.domain import model


def tag_factory():
    return [
        model.Tag('verbos'),
        model.Tag('vocabulario'),
        model.Tag('subtantivo'),
        model.Tag('gramatica')
    ]


def test_can_create_a_bunch_of_tags():
    assert tag_factory()


def test_can_create_guide_article():
    article = model.Article(
        title="Bem-vindos",
        description="Post de boas vindas",
        content="Este é o dama rowahutu!",
        category=model.Category.GUIDE,
        tags=tag_factory(),

    )

    assert article.category == model.Category.GUIDE


def test_can_create_short_article_with_timestamp():
    article = model.Article(
        title="Bem-vindos",
        description="Post de boas vindas",
        content="Este é o dama rowahutu!",
        category=model.Category.GUIDE,
        tags=tag_factory(),

    )

    assert article.created_on == datetime.now()
