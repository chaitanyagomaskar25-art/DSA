# Problem 1: Secret Number
# A security system receives a number from the user.
# If the number is greater than 100, print HIGH.
# If the number is less than 100, print LOW.
# If the number is exactly 100, print SAFE.
# Input: 125
# Output: HIGH

# n = int(input())
# if n >= 100:
#     if n == 100:
#         print("Safe")
#     else:
#         print("high")
# else:
#     print("low")


# Problem 2: Character Detector
# A system receives a single character.
# Determine whether the character is:
# an uppercase alphabet
# a lowercase alphabet
# a digit
# a special character
# Input: G
# Output: UPPERCASE

# c = input()

# if c.isupper():
#     print("UPPERCASE")
# elif c.islower():
#     print("lowercase")
# elif c.isdigit():
#     print("digit")
# else:
#     print("special character")



#  3: Password Strength
# A password is represented by its length.
# Less than 6 characters → Weak
# 6–9 characters → Medium
# 10 or more characters → Strong
# Input: 11
# Output: Strong 

# n = int(input())
# if n <6:
#     print("weak")
# elif n <= 9:
#     print("medium")
# else:
#     print("strong")