# 16.2 Множественное наследование
## Файл mro_slots.py содержит класс Product с дочерними классами Smartphone и LawnGrass
## c методом __add__ для сложения товаров из одинаковых классов продуктов и super() для расширения свойств
```    def __add__(self, other):
        if issubclass(type(other), self.__class__):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError
```

```
class Smartphone(Product):
    def __init__(
        self, name, price, quantity, description, efficiency, model, memory, color
    ):
        super().__init__(name, price, quantity, description)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name, price, quantity, description, color, country, germination_period
    ):
        super().__init__(name, price, description, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
```

### Также файл содержит абстрактный класс BaseProduct и миксин MixinLog
### Добавлен тест для миксина в test_mro_slots.py:

```def test_mixin_log_initialization():
    product = Product("Test Product", 100, 5, "Description")
    assert product.name == "Test Product"
    assert product.price == 100
    assert product.quantity == 5
    assert product.description == "Description"
```

### Функциональный код покрыт тестами на 99%.