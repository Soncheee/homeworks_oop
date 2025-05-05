class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = value

    @property
    def product(self):
        return f"Product(name={self.name}, price={self.__price}, quantity={self.quantity})"

    @classmethod
    def new_product(cls, params):
        """Создает новый объект Product из словаря параметров."""
        name = params.get('name')
        price = params.get('price')
        quantity = params.get('quantity')
        return cls(name, price, quantity)

class Category:
    def __init__(self, name):
        self.name = name
        self.__products = []

    @property
    def products(self):
        return self.__products

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise ValueError("Only Product instances can be added")

    @property
    def products_list(self):
        """Возвращает строку со списком товаров в формате: 'Название продукта, Цена руб. Остаток: Количество шт.'"""
        return '\n'.join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

# Пример использования
category = Category("Electronics")
product1 = Product("Smartphone", 599, 15)
product2 = Product("Laptop", 999, 40)

category.add_product(product1)
category.add_product(product2)

print(category.products_list)
