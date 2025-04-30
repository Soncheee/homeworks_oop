# 16.1 Наследование
## Файл classes.py содержит класс Product с дочерними классами Smartphone и LawnGrass
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

### Функциональный код покрыт тестами на 99%.