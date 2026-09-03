# Q1: Cricket Best Over Finder 🏏 ( Dont use max() )
# Given runs scored in each over, find which over scored the highest and how many runs.

# Input: [6, 12, 8, 15, 9, 4]
# Output: (3, 15)

# a = list(map(int, input().split()))
# m = 0
# i = 0
# for j in range(len(a)):
#     if a[j]> m:
#         m = a[j]
#         i = j
# print((i, m))

# ===============================================
# Q2: Alternate Positive/Negative Rearranger ➕➖ 
# Rearrange an array so positive and negative numbers alternate, starting with a positive number. If one type runs out, append the rest of the other type at the end.

# Input: [1, 2, -3, -1, 4, -5]
# Output: [1, -3, 2, -1, 4, -5]

# a = list(map(int, input().split()))
# b  =[] 
# p = [i for i in a if i >=0]
# n = [i for i in a if i < 0]

# l = 0
# r = 0
# while l < len(p) and r < len(n):
#     b.append(p[l])
#     b.append(n[r])
#     l+=1
#     r+=1
# b.extend(p[l:])
# b.extend(n[r:])
# print(b)

# ========================================++++++
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

# =====================================================================

# Q4: Permutation-in-String Checker 🔍
# Check if any rearrangement of a smaller string s1 exists as a substring inside a larger string s2. 

# Input: s1="ab", s2="eidbaooo"
# Output: True
# Explanation: ("ba" inside "eidbaooo" is a rearrangement of "ab") 

# s1 = input()
# s2 = input()

# for i in s1:
#     if i not in s2:
#         print("False")
#         break
# else:
#     print("True")