# Q1 Rectangle Area Function
# Write a simple function that takes the length and width of a rectangle and returns its area. This is meant to get you comfortable with defining a function, accepting parameters, and returning a value. 

# Input: length=5, width=3
# Output: 15

# def find_area(length, width):
#     return length*width
# l = int(input())
# w = int(input())
# print(find_area(l,w))


# ============================+++++

# Q2 Character Frequency Counter
# Count how many times each character appears in a string, and store the result in a dictionary.

# Input: "banana"
# Output: {'b': 1, 'a': 3, 'n': 2}

# s = input()
# freq = {}
# for i in s:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)

# ==========================================

# Q3 Find Common Elements Between Two Lists (Using Sets)
# Given two lists, find the elements that appear in both of them. 

# Input: [1,2,3,4,5], [3,4,5,6,7]
# Output: {3, 4, 5}

# HINT: Convert both lists to sets using set(), then use the & operator to get the intersection. 

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# a1 = set(a)
# a2 = set(b)
# print(a1 & a2)

# ==================================================

# Print an inverted right-angled triangle.

# Input

# 5

# Output

# * * * * *
# * * * *
# * * *
# * *
# *


# n = int(input())
# for i in range(n):
#     str = ""
#     for j in range(n-i):
#         str+="*"
#     print(str)

# ==========================

# Print a right-aligned triangle containing N rows.

# Input

# 5

# Output

#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# n = int(input())
# for i in range(n):
#     str = ""
#     for j in range(n-i):
#         str+=" "
#     for k in range(n-j):
#         str+="*"
#     print(str)

# ==========================

# Print a hollow square of size N. Only the boundary should contain stars.

# Input

# 5

# Output

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# n = int(input())
# for i in range(n):
#     str = ""
#     for j in range(n):
#         if i ==0 or i == n-1:
#             str+="*"
#         elif j == 0 or j == n-1:
#             str+="*"
#         else:
#             str+=" "
#     print(str)

# ===========================

# Q4 Three Sum: Zero-Sum Triplets 🎲
# Find all unique triplets in a list that add up to zero. No triplet should repeat, even if the same numbers appear via different indices.

# Input: [-1, 0, 1, 2, -1, -4]
# Output: [(-1, -1, 2), (-1, 0, 1)]


# HINT: Sort the array first (makes duplicates sit next to each other).

# a = list(map(int, input().split()))
# a.sort()
# n = len(a)
# result = set()
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             if a[i]+a[j]+a[k] == 0:
#                 result.add((a[i], a[j], a[k]))

# print(list(result))


# =============================================


# Q1 (Medium) — Snack Combo Pricing 🍿
# A cinema snack counter has these rules:
# Popcorn + Drink combo → ₹350
# Only Popcorn → ₹200
# Only Drink → ₹150
# Neither → ₹0
# Members get an extra 15% off on top of that (only if they ordered something).
# INPUT: popcorn=True, drink=True, is_member=True
# OUTPUT: 297.5

# p = input("Popcorn? (True/False): ").strip().lower() in ['true', '1']
# d = input("Drink? (True/False): ").strip().lower() in ['true', '1']
# m = input("Member? (True/False): ").strip().lower() in ['true', '1']

# if p == True:
#     if d== True:
#         if m== True:
#             print(350-(350*(15/100)))
#         else:
#             print(350)
#     else:
#         if m== True:
#             print(200-(200*(15/100)))
#         else:
#             print(200)
# elif d== True:
#     if m== True:
#         print(150-(150*(15/100)))
#     else:
#         print(150)
# else:
#     print("Invalid")

# =======================================================

# Q4 Set Matrix Zeroes 🔲
# Given a matrix, if any cell contains 0, set its entire row and entire column to 0.

# INPUT: 
# [[1, 1, 1],
#  [1, 0, 1],
#  [1, 1, 1]]

# OUTPUT:
# [[1, 0, 1],
#  [0, 0, 0],
#  [1, 0, 1]]

# a = [list(map(int, input().split())) for i in range(3)]

# for i in range(len(a)):
#     j = 0
#     while j < len(a):
#         if a[i][j] == 0:
#             a[0][j] = 0
#             a[1][j] = 0
#             a[2][j] = 0
#             a[i][0] = 0
#             a[i][1] = 0
#             a[i][2] = 0
#         j+=1
#         break
        
# print(a)

# =================================