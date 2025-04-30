import pytest
from src.magic_methods import Product, Category
@pytest.fixture
def product1():
    return Product("Smartphone", 599, 15)

@pytest.fixture
def product2():
    return Product("Laptop", 999, 40)

@pytest.fixture
def category(product1, product2):
    category = Category("Electronics")
    category.add_product(product1)
    category.add_product(product2)
    return category

# Тесты для класса Product
def test_product_initialization(product1):
    assert product1.name == "Smartphone"
    assert product1.price == 599
    assert product1.quantity == 15

def test_price_setter(product1):
    product1.price = 699
    assert product1.price == 699

    with pytest.raises(ValueError):
        product1.price = -10

def test_product_str(product1):
    assert str(product1) == "Smartphone, 599 руб. Остаток: 15 шт."

def test_addition_products(product1, product2):
    total_value = product1 + product2
    expected_value = (599 * 15) + (999 * 40)
    assert total_value == expected_value

def test_new_product_classmethod():
    params = {'name': 'Tablet', 'price': 299, 'quantity': 30}
    tablet = Product.new_product(params)
    assert tablet.name == "Tablet"
    assert tablet.price == 299
    assert tablet.quantity == 30

# Тесты для класса Category
def test_category_initialization(category):
    assert category.name == "Electronics"
    assert len(category.products) == 2

def test_add_product(category):
    product3 = Product("Tablet", 299, 30)
    category.add_product(product3)
    assert len(category.products) == 3

def test_products_list(category):
    expected_list = (
        "Smartphone, 599 руб. Остаток: 15 шт.\n"
        "Laptop, 999 руб. Остаток: 40 шт."
    )
    assert category.products_list == expected_list

def test_category_str(category):
    assert str(category) == "Electronics, количество продуктов: 55 шт."

