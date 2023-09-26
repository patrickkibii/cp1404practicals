def main():
    celsius = int(input("celsius: "))
    fahrenheit = int(input("fahrenheit: "))


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()
