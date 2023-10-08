import random

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 45
NUMBER_OF_QUICK_PICKS = 5
NUMBER_PER_PICK = 6


def main():
    number_quick_picks = int(input("How many quick picks: "))

    for number in range(number_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(map(str, quick_pick)))


def generate_quick_pick():
    return sorted(random.sample(range(MINIMUM_RANDOM_NUMBER , MAXIMUM_RANDOM_NUMBER + 1), NUMBER_PER_PICK))


main()


