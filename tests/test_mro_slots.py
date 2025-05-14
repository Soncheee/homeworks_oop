import pytest


from src.mro_slots import Category, LawnGrass, Product, Smartphone

def test_mixin_log_initialization():
    product = Product("Test Product", 100, 5, "Description")
    assert product.name == "Test Product"
    assert product.price == 100
    assert product.quantity == 5
    assert product.description == "Description"


def test_product_initialization():
    product = Product("Test Product", 100.0, 5, "Test Description")
    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.quantity == 5
    assert product.description == "Test Description"


def test_price_property():
    product = Product("Test Product", 100.0, 5, "Test Description")
    assert product.price == 100.0


def test_price_setter():
    product = Product("Test Product", 100.0, 5, "Test Description")
    product.price = 150.0
    assert product.price == 150.0

    with pytest.raises(ValueError):
        product.price = -10


def test_product_property():
    product = Product("Test Product", 100.0, 5, "Test Description")
    expected_output = "Product(name=Test Product, price=100.0, quantity=5)"
    assert product.product == expected_output


def test_new_product_classmethod():
    params = {
        "name": "New Product",
        "price": 200.0,
        "quantity": 10,
        "description": "New Description",
    }
    new_product = Product.new_product(params)
    assert new_product.name == "New Product"
    assert new_product.price == 200.0
    assert new_product.quantity == 10
    assert new_product.description == "New Description"


def test_str_method():
    product = Product("Test Product", 100.0, 5, "Test Description")
    expected_output = "Test Product, 100.0 руб. Остаток: 5 шт."
    assert str(product) == expected_output


def test_add_method():
    product1 = Product("Product 1", 100.0, 5, "Description 1")
    product2 = Product("Product 2", 200.0, 3, "Description 2")
    result = product1 + product2
    expected_result = (100.0 * 5) + (200.0 * 3)
    assert result == expected_result

    with pytest.raises(TypeError):
        product1 + "Invalid Type"


def test_category_initialization():
    category = Category("Test Category", 'Category')
    assert category.name == "Test Category"
    assert category.description == 'Category'
    assert category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product():
    category = Category("Test Category", 'Category')
    product1 = Product("Product 1", 100.0, 5, "Description 1")
    product2 = Product("Product 2", 200.0, 10, "Description 2")

    category.add_product(product1)
    assert len(category.products) == 1
    assert Category.product_count == 1

    category.add_product(product2)
    assert len(category.products) == 2
    assert Category.product_count == 2

    with pytest.raises(TypeError):
        category.add_product("Invalid Product")


def test_products_list():
    category = Category("Test Category", 'Category')
    product1 = Product("Product 1", 100.0, 5, "Description 1")
    product2 = Product("Product 2", 200.0, 10, "Description 2")

    category.add_product(product1)
    category.add_product(product2)
    expected_output = (
        "Product 1, 100.0 руб. Остаток: 5 шт.\nProduct 2, 200.0 руб. Остаток: 10 шт."
    )
    assert category.products_list == expected_output


def test_category_str_method():
    category = Category("Test Category", 'Category')
    product1 = Product("Product 1", 100.0, 5, "Description 1")
    product2 = Product("Product 2", 200.0, 10, "Description 2")

    category.add_product(product1)
    category.add_product(product2)
    expected_output = "Test Category, количество продуктов: 15 шт."
    assert str(category) == expected_output


def test_smartphone_initialization():
    smartphone = Smartphone(
        "Smartphone",
        599.0,
        15,
        "A great smartphone",
        "High",
        "Model X",
        "128GB",
        "Black",
    )
    assert smartphone.name == "Smartphone"
    assert smartphone.price == 599.0
    assert smartphone.quantity == 15
    assert smartphone.description == "A great smartphone"
    assert smartphone.efficiency == "High"
    assert smartphone.model == "Model X"
    assert smartphone.memory == "128GB"
    assert smartphone.color == "Black"


def test_lawn_grass_initialization():
    lawn_grass = LawnGrass(
        "Lawn Grass", 10.0, "Green grass", 50, "Green", "USA", "7 days"
    )
    assert lawn_grass.name == "Lawn Grass"
    assert lawn_grass.price == 10.0
    assert lawn_grass.quantity == 50
    assert lawn_grass.description == "Green grass"
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "7 days"
    assert lawn_grass.color == "Green"


def test_middle_price_category():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 7)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 10)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 6)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    assert category1.middle_price() == 0

    category_empty = Category("Смартфоны", "Категория смартфонов",[])
    assert category_empty.middle_price() == 0