total = 0
items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items")
    items = int(input("Number of items: "))
for i in range(items):
    price = int(input("Price: "))
    total = price + total
if total > 100:
    discount = total * 0.1
    total = total - discount
print(f'Total price for {items} items is {total:.2f}')
