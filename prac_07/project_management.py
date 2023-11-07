import datetime
from project import Project

FILENAME = "projects.txt"


def main():
    # projects = load_projects(FILENAME)
    display_menu()
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            projects = load_projects(FILENAME)
            print("Loaded Successfully")
            display_menu()
            choice = input(">>> ").lower()
        elif choice == "s":

            display_menu()
            choice = input(">>> ").lower()
        elif choice == "d":
            display_projects(projects)
            display_menu()
            choice = input(">>> ").lower()
        elif choice == "f":

            display_menu()
            choice = input(">>> ").lower()
        elif choice == "a":

            display_menu()
            choice = input(">>> ").lower()
        elif choice == "u":
            update_project(projects)
            display_menu()
            choice = input(">>>").lower()
        else:
            print("Invalid menu choice")
            print("Menu:\nD - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit")
            choice = input(">>>").lower()
    # save_songs(songs, FILENAME)
    # print(f"{len(songs)} songs loaded")
    # print("Make some music!!!")
    # display_songs(songs)


def display_menu():
    print(
        "- (L)oad projects  \n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by \n- (A)dd new project\n- "
        "(U)pdate project\n- (Q)uit")


def load_projects(filename):
    projects = []
    # Open the file for reading
    in_file = open(filename, 'r')
    # File format is like: Name	Start Date	Priority	Cost Estimate	Completion Percentage
    in_file.readline()
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split('\t')
        # print(parts)  # debugging
        # Reflection is stored as a string (Yes/No) and we want a Boolean
        # pointer_arithmetic = parts[3] == "Yes"
        # reflection = parts[2] == "Yes"
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()
    return projects
    # for line in projects:
    #     print(line)


def save_projects():
    pass


def display_projects(filename):
    completed_projects = []
    incomplete_projects = []
    for project in filename:
        # print(project)  # debugging
        if project.is_complete():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
            # print("Incomplete projects:")
            # print(project)
    print("Completed projects: ")
    for project in completed_projects:
        print(project)
    print("Incomplete Projects")
    for project in incomplete_projects:
        print(project)


def filter_projects_by_date():
    pass


def add_project():
    print("Let's add a new project")


def update_project(projects):
    for i, project in enumerate(projects):
        print(i, project)
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])

    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    if project_choice != "" and new_priority != "" and new_percentage != "":
        projects[project_choice][4] = new_percentage
        projects[project_choice][2] = new_priority


main()
