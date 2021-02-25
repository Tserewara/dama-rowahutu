from src.articles.services import category_service


def test_category_exists():
    assert category_service.get_category(1)
    assert not category_service.get_category(999)
