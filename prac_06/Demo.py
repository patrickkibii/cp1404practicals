class MyClass:
    def __init__(self, height, weight):
        self.height = height
        self.uzito = weight

    def __str__(self):
        return f"Height:{self.height} weight: {self.uzito}"

    def MyFunction(self):
        print(f"Saka knee gear " + str(self.uzito))


p1 = MyClass(23, 100)

# print(p1)
# p1.MyFunction()

products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
on_sale_products = [product for product in products if product[2]]
print(on_sale_products)