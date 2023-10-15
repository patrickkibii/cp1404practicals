COLORS = {"aliceblue": "#f0f8ff", "black": "#000000", "red": "#ff0000", "green": "#008000", "blue": "#0000ff",
          "white": "#ffffff", "yellow": "#ffff00", "purple": "#800080", "pink": "#ffc0cb", "orange": "#ffa500", }
color_name = input("Input color name: ").strip().lower()
while color_name != "":
    if color_name in COLORS:
        print(color_name, "is", COLORS[color_name])
    else:
        print("Invalid short state")
    color_name = input("INPUT color name: ").strip().lower()

print("Good Bye")
