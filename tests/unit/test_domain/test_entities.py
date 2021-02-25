from src.articles.domain.entities import category, article, tag


def tag_factory():
    return [
        tag.Tag('verbos'),
        tag.Tag('vocabulario'),
        tag.Tag('subtantivo'),
        tag.Tag('gramatica')
    ]


def test_can_create_a_bunch_of_tags():
    assert tag_factory()


def test_can_create_guide_article():
    _article = article.Article(
        title="Bem-vindos",
        description="Post de boas vindas",
        content="Este é o dama rowahutu!",
        category=category.Category.GUIDE,
        tags=tag_factory(),

    )

    assert _article.category == category.Category.GUIDE


def test_can_create_short_article_with_timestamp():
    _article = article.Article(
        title="Bem-vindos",
        description="Post de boas vindas",
        content="Este é o dama rowahutu!",
        category=category.Category.GUIDE,
        tags=tag_factory(),

    )

    assert _article.created_on
