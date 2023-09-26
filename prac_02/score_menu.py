def main():
    """Get a score print results and stars"""
    print("(G)et a valid score (P)rint result (S)how stars (Q)uit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
            print(get_result(score))
        elif choice == "P":
            result = get_result(score)
            print(result)
        elif choice == "S":
            print_asterisks(score)
        print("(G)et a valid (P)rint result (S)how stars (Q)uit")
        choice = input(">>> ").upper()
    print("Bye")


def get_result(score):
    """Get result from score"""
    if score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score > 0:
        return "Bad"
    else:
        return "Invalid Score"


def print_asterisks(score):
    """Display line of stars"""
    print("*" * score)


main()
