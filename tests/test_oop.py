from src.oop_homework import Product, Category
import pytest

@pytest.fixture
def new_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 5, 180000.0)

@pytest.fixture
def new_category():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 5, 180000.0)
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
                    [product1, ])

def test_product_init(new_product):
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.quantity == 5
    assert new_product.price == 180000.0

def test_category_init(new_category):
    assert new_category.name == 'Смартфоны'
    assert new_category.description == ('Смартфоны, как средство не только коммуникации, '
                                        'но и получения дополнительных функций для удобства жизни')
    assert len(new_category.products) == 1
    assert Category.total_category == 1
    assert Category.total_products == 1

def test_multiple_categories(new_category):
    # Создаем еще одну категорию для проверки
    product2 = Product("iPhone 15", "128GB, Черный цвет, 50MP камера", 3, 150000.0)
    category2 = Category("Смартфоны", "Новая категория", [product2])

    assert Category.total_category == 3
    assert Category.total_products == 3