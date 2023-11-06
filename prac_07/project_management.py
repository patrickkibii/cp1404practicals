import datetime


def main():
    display_menu()
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":

            display_menu()
            choice = input(">>>").lower()
        elif choice == "s":

            display_menu()
            choice = input(">>>").lower()
        elif choice == "d":

            display_menu()
            choice = input(">>>").lower()
        elif choice == "f":

            display_menu()
            choice = input(">>>").lower()
        elif choice == "a":

            display_menu()
            choice = input(">>>").lower()
        elif choice == "u":

            display_menu()
            choice = input(">>>").lower()
        else:
            print("Invalid menu choice")
            print("Menu:\nD - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit")
            choice = input(">>>").lower()
    save_songs(songs, FILENAME)
    print(f"{len(songs)} songs loaded")
    print("Make some music!!!")
    display_songs(songs)


def display_menu():
    print("- (L)oad projects  \n- (S)ave projects\n- (D)isplay projec\n- (F)ilter projects by \n- (A)dd new project\n- "
          "(U)pdate project\n- (Q)uit")


def load_projects():
    pass


def save_projects():
    pass


def display_projects():
    pass


def filter_projects_by_date():
    pass


def add_project():
    pass


def update_project():
    pass


main()
