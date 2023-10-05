# file_name = input("File Name: ")
# in_file = open(file_name)
# for line in in_file:
#     print(line)

# s = "\tPython, Monty \n"
# print(s[1], ".", sep="")
# print(s.strip(), ".", sep="")
# s.replace(' ', '*')
# print(s.lstrip(), ".", sep="")
# print(s.strip().split(','))

# name = input("Name: ")
# out_file = open(name, "w")
# print(name)
# out_file.close()
#
#
# name = input("Name")
# with open(name, "w") as out_file:
#     print(name)

# filename = 'usernames.txt'
# in_file = open(filename, 'r')
# for line in in_file:
#     if line[0] == '#':
#         print("Mark down file : Heading 1 ")
#         print(line)
#     else:
#         print(f"Good morning {line}")


# print(in_file.read(100))


# x = str(int('1.0'))
# x[-1] = '2'
# x = str(1.0)
# x[-1] = '2'
try:
    x = int("zero")
    print(10 / x)
except ZeroDivisionError:
    print("div")
except NameError:
    print("name")
except ValueError:
    print("value")
except:
    print("other")



