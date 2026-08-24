# 1. Find User with Longest Username
# Problem
# Given a list of usernames, return the longest username.
# Input
# [
# "riya",
# "rinkinisha",
# "amit",
# "john"
# ]
# Expected Output
# rinkinisha

# a = list(map(str, input().split()))
# m = 0
# n = ""
# for i in a:
#     if len(i) > m:
#         m = len(i)
#         n = i
# print(n)

# ===========================================
# Ques1: License Plate Palindrome Checker 🚗 (Using Loops)
# A license plate is called a palindrome if it reads the same forwards and backwards.
# Write a function to check if a given plate number is a palindrome.

# INPUT: "RACECAR"
# OUTPUT: True
# INPUT: "DL8CAF9"
# OUTPUT: False

# def palindrome_checker(s):
#     s = s.lower()
#     l = 0
#     r = len(s)-1
#     while l<=r:
#         if s[l]!=s[r]:
#             return False
#         l+=1
#         r-=1
#     return True

# print(palindrome_checker("RACECAR"))

# ===================================
# Ques3: Movie Ticket Price Calculator 🎟️ 
# A cinema calculates ticket price using these rules:
# Age below 5 → Base price ₹0 (free)
# Age 5–11 → Base price ₹150
# Age 60 or above → Base price ₹100
# Everyone else → Base price ₹250
# On top of that:
# If it's a weekend, add ₹50 to the price
# If the person has a student card AND is between 12–59 years old, subtract ₹50

# Write a function ticket_price(age, is_weekend, has_student_card) that returns the final price. 
# INPUT: age = 25, is_weekend = True, has_student_card = True
# OUTPUT: 250

# def ticket_price(age, is_weekend, has_student_card):
#     if age < 5:
#         if is_weekend:
#             print("₹50")
#         else:
#             print("₹0")
#     elif age >= 5 and age <= 11:
#         if is_weekend:
#             print("₹200")
#         else:
#             print("₹150")
#     elif age >= 60:
#         if is_weekend:
#             print("₹150")
#         else:
#             print("₹100")
#     else:
#         if age >= 12 and age < 60:
#             if is_weekend:
#                 if has_student_card:
#                     print("₹250") 
#                 else:
#                     print("₹300")
#             else:
#                 if has_student_card:
#                     print("₹200")
#                 else:
#                     print("₹250")

# ticket_price(25,True, True)


# ================================


# Q1: Missing Number Detective 🕵️
# An array contains numbers from 1 to n, but one number is missing. 
# Find it — without sorting the array.

# INPUT: [1, 2, 4, 5, 6, 7, 8] , here (n = 8)
# OUTPUT: Missing number: 3

# a = list(map(int, input().split()))
# newArr = [i for i in range(1, max(a)+1)]

# for i in newArr:
#     if i not in a:
#         print(i, end=" ")
# print("")

# =====================================
# Q2: Matrix Diagonal Difference 🔲
# Given a square matrix, find the absolute difference between the sum of its main diagonal (top-left to bottom-right) and its secondary diagonal (top-right to bottom-left).

# INPUT: 
# [[11, 2, 4],
#  [4, 5, 6],
#  [10, 8, -12]]
# OUTPUT: Absolute difference: 15
# (main diagonal: 11+5-12 = 4 | secondary: 4+5+10 = 19 | |4-19| = 15) 


# n = int(input())
# a = []
# for i in range(n):
#     newArr = list(map(int, input().split()))
#     a.append(newArr)

# s = 0
# p = 0
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             p+= a[i][j]
#         if j == n-i-1:
#             s+=a[i][j]
# print(abs(p-s))


# ======================================
# Q3: All Pairs Summing to Target 🎯 
# Given a list of numbers and a target value, find all pairs of indices (i, j) where the two numbers add up to the target. Each number can only be used once per pair (don't reuse the same index in two different pairs).

# INPUT: arr = [2, 7, 11, 15, 5, 9] , target = 9
# OUTPUT: [(0, 1)]

# a = list(map(int, input().split()))
# t = int(input())
# n =[]
# used = set()
# s = 0
# f = 1
# while s < len(a):
#     if s in used:
#         s+=1
#         continue
    
#     f = s+1
#     while f < len(a):
#         if f in used:
#             f+=1
#             continue
        
#         if a[s]+a[f] == t:
#             n.append((s,f))
#             used.add(s)
#             used.add(f)
#             break
#         f+=1
#     s+=1
      
# print(n)

# ===================================
# Q4: Matrix Spiral Traversal 🌀
# Given a square (or rectangular) matrix, print all its elements in spiral order — starting from the top-left, moving right, then down, then left, then up, and spiraling inward.

# INPUT:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

# OUTPUT: [1, 2, 3, 6, 9, 8, 7, 4, 5]

# n = int(input("Enter the no of rows: "))
# m = int(input("Enter the no of column: "))
# a = []
# for i in range(n):
#     newArr = []
#     for j in range(m):
#         num = int(input())
#         newArr.append(num)
#     a.append(newArr)

# t = 0
# b = n-1
# l = 0
# r = m-1
# result = []


# while l<=r and t<=b:
#     for cols in range(l, r+1):
#         result.append(a[t][cols])
#     t+=1
#     for rows in range(t, b+1):
#         result.append(a[rows][r])
#     r-=1
#     if t<=b:
#         for cols in range(r, l-1, -1):
#             result.append(a[b][cols])
#         b-=1
#     if l<=r:
#         for rows in range(b, t-1, -1):
#             result.append(a[rows][l])
#         l +=1
# print(result)

