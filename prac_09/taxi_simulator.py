from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Chrysler", 90, 4), SilverServiceTaxi("Dodge", 200, 4),
             SilverServiceTaxi("Chevrolet", 250, 1)]
    bill = 0
    current_taxi = None
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>>").lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis are available:")
            list_taxis(taxis)
            taxi_choice = int(input("Pick a Taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid Choice")
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                current_taxi.drive(int(input("Drive how far? ")))
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                bill += trip_cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>>").lower()
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    list_taxis(taxis)


def list_taxis(taxis):
    return [print(f"{i} - {taxi}") for i, taxi in enumerate(taxis)]


main()
