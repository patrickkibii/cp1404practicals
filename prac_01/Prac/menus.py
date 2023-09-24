name = input("Name: ")
print("(H)ello (G)oodbye (Q)uit")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("invalid Message")
    print("(H)ello (G)oodbye (Q)uit")
    
    choice = input(">>> ").upper()
print("Finished.")
