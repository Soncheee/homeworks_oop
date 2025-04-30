class Product:
    # name: str
    # description: str
    # quantity: int
    # price: float

    def __init__(self, name, description, quantity, price):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price



class Category:
    total_category = 0
    total_products = 0
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.total_category += 1
        Category.total_products += len(self.products)
