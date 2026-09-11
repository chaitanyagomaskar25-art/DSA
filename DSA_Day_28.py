# Q1: Count Uppercase Letters 🔠
# Count how many uppercase letters appear in a sentence. 

# Input: "Hello World From India"
# Output: 4

# s = input("Enter a sentence: ")
# c = 0
# for i in s:
#     if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         c+=1
# print(c)

# ===============================

# Q2: Count Words Starting with a Vowel 🔤
# Count how many words in a sentence start with a vowel. 

# Input: "Akriti is eating an apple today"
# Output: 5
# s = input("Enter a sentence: ")
# c = 0
# if s[0] in "AEIOUaeiou":
#     c+=1

# for i in range(len(s)):
#     if s[i] == " ":
#         if s[i+1] in "AEIOUaeiou":
#             c+=1
# print(c)

# =============================================


# Q4: Diamond Star Pattern 💎: 
# Print a diamond shape made of stars, given the number of rows for the top half.

# Input: n=4
# Output:


#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    * 

# n = int(input("Enter a number: "))

# for i in range(n):
#     str=""
#     for j in range(n - i - 1):
#         str+=" "
#     for k in range(2 * i + 1):
#         str+="*"
#     print(str)

# for i in range(n-2, -1, -1):
#     str=""
#     for j in range(n - i - 1):
#         str+=" "
#     for k in range(2 * i + 1):
#         str+="*"
    
#     print(str)
    

# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))
# for i in range(n - 2, -1, -1 ):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))
    