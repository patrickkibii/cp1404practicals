EMAIL_TO_NAME = {}


def extract_name(email):
    name = email.split('@')[0]
    name = name.title()
    return name


email = input("Email: ")
while email != "":
    name = extract_name(email)
    name_confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
    if name_confirmation not in ('', 'y', 'yes'):
        name = input("Name: ")
    EMAIL_TO_NAME[email] = name
    email = input("Email: ")


for email, name in EMAIL_TO_NAME.items():
    print(f"{name} ({email})")



