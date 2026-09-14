# Q1: Cricket Best Over Finder 🏏 ( Dont use max() )
# Given runs scored in each over, find which over scored the highest and how many runs.

# Input: [6, 12, 8, 15, 9, 4]
# Output: (3, 15)

# a = list(map(int, input().split()))
# m = a[0]
# index = 0
# for i in range(len(a)):
#     if a[i] > m:
#         m = a[i]
#         index = i
    
# print((index, m))


# ===================================================
# Q2: Alternate Positive/Negative Rearranger ➕➖ 
# Rearrange an array so positive and negative numbers alternate, starting with a positive number. If one type runs out, append the rest of the other type at the end.

# Input: [1, 2, -3, -1, 4, -5]
# Output: [1, -3, 2, -1, 4, -5]
# a = list(map(int, input().split()))
# p = []
# n = []
# result = []

# for i in a:
#     if i >= 0:
#         p.append(i)
#     else: 
#         n.append(i)

# i =0
# j =0
# while i < len(p) and j < len(n):
#     result.append(p[i])
#     result.append(n[j])
#     i+=1
#     j+=1
# result.extend(p[i:])
# result.extend(n[j:])
# print(result)

# ==================================

# Q3: Product of Array Except Self ✖️
# Given an array, return a new array where each element is the product of all other elements (excluding itself) — without using division.

# Input: [1, 2, 3, 4]                                                                                                                                                                                                                                                                                                                                                                                                                                           
 
# Output: [24, 12, 8, 6]

# a = list(map(int, input().split()))
# result = []
# for i in range(len(a)):
#     p = 1
#     for j in range(len(a)):
#         if i != j:
#             p*=a[j]
#     result.append(p)
# print(result)


# ========================================
# Q1: Name Initials Generator (String + Function)
# Take a person's full name (lowercase words separated by spaces) and turn it into initials like "A.K.S.". 

# Input: "aman kumar sharma"
# Output: "A.K.S."

# s = input()
# a = s.split()
# for i in a:
#     print(i[0].upper(), end=".")
# print()

# ========================================
