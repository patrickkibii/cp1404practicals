# COLORS = {"aliceblue": "#f0f8ff", "black": "#000000", "red": "#ff0000", "green": "#008000", "blue": "#0000ff",
#           "white": "#ffffff", "yellow": "#ffff00", "purple": "#800080", "pink": "#ffc0cb", "orange": "#ffa500", }
COLORS = {"AbsoluteZero": "#0048ba",
          "AcidGreen": "#b0bf1a",
          "AliceBlue": "#f0f8ff",
          "AlizarinCrimson": "#e32636",
          "Amaranth": "#e52b50",
          "Amber": "#ffbf00",
          "Amethyst": "#9966cc",
          "AntiqueWhite": "#faebd7",
          "AntiqueWhite1": "#ffefdb",
          "AntiqueWhite2": "#eedfcc",
          "AntiqueWhite3": "#cdc0b0",
          "AntiqueWhite4": "#8b8378",
          "Apricot": "#fbceb1",
          "Aqua": "#00ffff"
          }
color_name = input("Input color name: ").strip().lower()
while color_name != "":
    if color_name in COLORS:
        print(color_name, "is", COLORS[color_name])
    else:
        print("Invalid short state")
    color_name = input("INPUT color name: ").strip().lower()

print("Good Bye")
