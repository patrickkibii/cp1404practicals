"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)
    name = "limo"
    limo = Car(100)
    fuel_to_add = 20
    limo.add_fuel(fuel_to_add)
    print("Added {} units of fuel.".format(fuel_to_add))
    distance_to_drive = 100
    limo.drive(distance_to_drive)


main()