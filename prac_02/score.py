"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = get_result()
    score = random.randint(100)
    print(result)


def get_result(score):
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
