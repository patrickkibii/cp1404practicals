"""
Client code.
"""
from prac_06.guitar import Guitar


def play_guitars():
    guitars = []
    name = input("Name: ")
    while name != "":
        cost = float(input("Cost: $"))
        year = int(input("Year: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "has been added successfully")
        name = input("Name: ")

    if guitars:
        guitars.sort()
        print("Here are my guitars: ")
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1.name:>30}, ({1.year}) worth ${1.cost:,.2f} {2}".format(i + 1, guitar, vintage_string))
    else:
        print("Invalid")


if __name__ == '__main__':
    play_guitars()