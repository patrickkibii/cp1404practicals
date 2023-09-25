for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 101, 10):
    print(i, end=" ")
print()
for i in range(20, 0, -1):
    print(i, end=" ")
print()

stars = int(input("Number of stars: "))
for i in range(stars+1):
    print("*", end=" ")
print()

lines = int(input("Input Number Of Lines: "))

for i in range(1, lines+1):
    for j in range(i):
        print('*', end='')
    print()

