import pytest

from src.access_modes import Category, Product
def test_create_product():
    product = Product("Smartphone", 599, 15)
    assert product.name == "Smartphone"
    assert product.price == 599
    assert product.quantity == 15

def test_new_product_method():
    params = {'name': 'Laptop', 'price': 999, 'quantity': 40}
    product = Product.new_product(params)
    assert product.name == "Laptop"
    assert product.price == 999
    assert product.quantity == 40

def test_price_setter():
    product = Product("Smartphone", 599, 15)
    product.price = 699
    assert product.price == 699

    with pytest.raises(ValueError):
        product.price = -10

def test_add_product_to_category():
    category = Category("Electronics")
    product = Product("Smartphone", 599, 15)
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == product

def test_products_list():
    category = Category("Electronics")
    product1 = Product("Smartphone", 599, 15)
    product2 = Product("Laptop", 999, 40)
    category.add_product(product1)
    category.add_product(product2)
    expected_output = "Smartphone, 599 руб. Остаток: 15 шт.\nLaptop, 999 руб. Остаток: 40 шт."
    assert category.products_list == expected_output

def test_add_invalid_product():
    category = Category("Electronics")
    with pytest.raises(ValueError):
        category.add_product("Not a product")
