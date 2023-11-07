import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file of guitars details, save as objects, display."""
    guitars = []
    in_file = open(FILENAME, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()

    for guitar in guitars:
        print(guitar)

    # add_guitar(guitars)
    added_guitars = add_guitar(guitars)
    save_guitars(added_guitars)


def add_guitar(guitars):
    """Add guitar to guitars list"""
    new_guitar = []
    print("Enter details for new guitar.")
    name = input("Name: ")
    cost = input("Cost: ")
    year = 0
    while year <= 0:
        if name == "" or cost == "":
            print("Input can not be blank")
            name = input("Name: ")
            cost = input("Cost: ")
            return
        try:
            year = int(input("Year: "))
        except ValueError:
            print("Invalid input; enter a valid number")
            year = int(input("Year: "))
    new_guitar = [name, year, cost]
    guitars.append(new_guitar)
    print(f"{name} added to guitar list.")
    return guitars


def save_guitars(guitars):
    """Write guitars to a file"""
    with open("guitars.csv", "w", newline="") as out_file:
        for guitar in guitars:
            print(f"{guitar}", file=out_file)


# def get_guitars(filename):
#     guitars = []
#     in_file = open(filename, 'r')
#     for line in in_file:
#         parts = line.strip().split(',')
#         name = parts[0]
#         year = int(parts[1])
#         cost = float(parts[2])
#         guitar = [name, year, cost]
#         guitars.append(guitar)
#     in_file.close()


main()
