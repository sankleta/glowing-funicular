#!/bin/python3

import string


def getStrength(password, weight_a):
    weight = weight_a
    letter_weights = {}
    for letter in "abcdefghijklmnopqrstuvwxyz":
        letter_weights[letter] = weight
        if weight == 25:
            weight = 0
        else:
            weight += 1
    strength = 0
    for letter in password:
        strength += letter_weights[letter.lower()]
    return strength


if __name__ == '__main__':
    password = input()

    weight_a = int(input().strip())

    strength = getStrength(password, weight_a)

    print(str(strength) + '\n')
