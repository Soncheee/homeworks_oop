class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, price, quantity, description):
        self.name = name
        self.__price = price
        self.quantity = quantity
        self.description = description

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
        return (
            f"Product(name={self.name}, price={self.__price}, quantity={self.quantity})"
        )

    @classmethod
    def new_product(cls, params):
        """Создает новый объект Product из словаря параметров."""
        name = params.get("name")
        price = params.get("price")
        quantity = params.get("quantity")
        description = params.get("description")  # Добавляем description
        return cls(name, price, quantity, description)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if issubclass(type(other), self.__class__):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name):
        self.name = name
        self.__products = []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        return self.__products

    def add_product(self, other):
        if isinstance(other, Product):
            self.__products.append(other)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products_list(self):
        """Возвращает строку со списком товаров в формате: 'Название продукта, Цена руб. Остаток: Количество шт.'"""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


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
