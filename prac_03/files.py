# 1
name = input("Name: ")
out_file = open('name.txt', 'w')
out_file.write(name)
out_file.close()

# 2
file_name = "name.txt"
in_file = open(file_name, 'r')
for line in in_file:
    print(f'Your name is {line}')
in_file.close()

# 3
with open('numbers.txt', 'r') as in_file:
    numbers = in_file.readlines()
    total = int(numbers[0]) + int(numbers[1])
    print(f"Total: {total}")


#4

in_file = open('numbers.txt', 'r')
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(f"Total: {total}")
