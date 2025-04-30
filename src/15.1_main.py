from magic_methods import Product, Category

if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", 180000.0, 5)
    product2 = Product("Iphone 15", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))



    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)