class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def apply_discount(self, discount_type):
        return discount_type.apply(self.price)

    

class SeasonalDiscount:


    def apply(self, price):
        return price * 0.5
    

product = Product(name = "fevical", price=200)

print(product.apply_discount(SeasonalDiscount()))