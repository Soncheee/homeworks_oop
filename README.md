# 14.1 Введение в ООП
## Содержит модули main.py, oop_homework.py, test_oop.py
### *oop_homework.py:*
### Созданы классы Product, Category
```class Product:
    # name: str
    # description: str
    # quantity: int
    # price: float

    def __init__(self, name, description, quantity, price):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
```
```class Category:
    total_category = 0
    total_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

    def category_count(self):
        Category.total_category += 1
    def product_count(self):
        Category.total_products += len(self.products)
```
### *test_oop.py*
### Написаны тесты, которые проверяют корректность инициализации объектов класса *Category*
``` def test_category_init(new_category):
    assert new_category.name == 'Смартфоны'
    assert new_category.description == ('Смартфоны, как средство не только коммуникации, '
                                        'но и получения дополнительных функций для удобства жизни')
    assert len(new_category.products) == 1
    assert Category.total_category == 0
    assert Category.total_products == 0
```
### Написаны тесты, которые проверяют корректность инициализации объектов класса *Product*
```def test_product_init(new_product):
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.quantity == 5
    assert new_product.price == 180000.0
```

![](https://i.pinimg.com/736x/50/ed/2f/50ed2fdd65f3147bfdb519870e21aaf0.jpg)