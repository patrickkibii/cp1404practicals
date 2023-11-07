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
            save_projects(projects)
            display_menu()
            choice = input(">>> ").lower()
        elif choice == "d":
            display_projects(projects)
            display_menu()
            choice = input(">>> ").lower()
        elif choice == "f":
            filter_projects_by_date()
            display_menu()
            choice = input(">>> ").lower()
        elif choice == "a":
            add_project(projects)
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
    print("Thank you for using custom-built project management software.")


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


def save_projects(projects):
    """Write projects to a file"""
    filename = input("Input File Name to Save to: ")
    with open(filename, "w", newline="") as out_file:
        for project in projects:
            print(project, file=out_file)


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
    # date_input = input("Show projects that start after date (dd/mm/yy): ")
    # x = date_input.strip().split('/')
    # filter_date = int(x[0]), int(x[1]), int(x[2])
    # print(filter_date)
    # import datetime

    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(f"That day is/was {date.strftime('%A')}")
    print(date.strftime("%d/%m/%Y"))


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start Date: ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion = input("Percent Complete: ")
    # Project(name, start_date, priority, cost_estimate, completion)
    # projects.append(Project)
    project = Project(name, start_date, int(priority), float(cost_estimate), int(completion))
    projects.append(project)


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
# filter_projects_by_date()
