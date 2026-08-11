# Mathison and pangrams (1127)

# t = int(input())

# for _ in range(t):
#     n = list(map(int, input().split()))
#     s = input()
#     r = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     s = set(s)
#     s = list(sorted(s))
#     c = 0
#     j = 0
#     for i in range(26):
#         if j<len(s) and s[j] == r[i]:
#             j+=1
#         else:
#             c += n[i]
#     print(c)

# ============================

# Valid Minimum (1132)

# t = int(input())

# for _ in range(t):
#     a = list(map(int, input().split()))
#     a = sorted(a)
#     if a[0] == a[1]:
#         print("yes")
#     else:
#         print("no")

# ===============================

    
# 1.Traffic Jam Detector 🚗
# A road has N checkpoints. At each checkpoint, the number of vehicles is recorded.
# A checkpoint is considered congested if the number of vehicles is greater than both the previous and next checkpoint.
# Find the number of congested checkpoints.
# Input: 10 25 18 30 20 15 28 12
# Output: 3

# a = list(map(int, input().split()))
# c = 0
# for i in range(1, len(a)-1):
#     if a[i-1] < a[i] and a[i+1] < a[i]:
#         c +=1
# print(c)

# =====================


# Power Consumption 🔋
# A device records its power consumption every hour.
# Find the longest continuous period during which power consumption keeps increasing.
# Input: 10 15 20 18 22 25 30 17
# Output: 4

# a = list(map(int, input().split()))
# c = 0
# max = 0

# for i in range(len(a)-1):
#     for j in range(i+1, len(a)-1):
#         if a[i] < a[j] and a[j] > a[j-1]:
#             c+=1
#         else:
#             break
#     if c > max:
#         max = c 
#         c = 0
# print(max)

# =============================

# 3.Balanced Array ⚖️
# An array is called balanced at index i if the sum of all elements before i is equal to the sum of all elements after i.
# Find the first balanced index.
# Input: 1 2 3 6 2 4
# Output: 3

# a = list(map(int, input().split()))
# c = 0
# for i in range(len(a)):
#     sumB = sum(a[:i])
#     sumA = sum(a[i+1:])
#     if sumB == sumA:
#         print(i)

# =========================

# There are 5 products.
# Create two arrays:
# One array stores the MRP.
# Another array stores the Discount Percentage.
# Using arrays:
# Calculate the selling price of every product.
# Display the selling price.

# m = list(map(int, input().split()))
# d = list(map(int, input().split()))

# for i in range(len(m)):
#     selling = m[i] - (m[i]*(d[i]/100))
#     print(int(selling))


# ===============================

# Store the MRP and Discount of 6 products in arrays.
# For every product:
# If the discount is between 0 and 100, calculate the selling price.
# Otherwise print "Invalid Discount".

# m = list(map(int, input().split()))
# d = list(map(int, input().split()))

# for i in range(len(m)):
#     if d[i] > 0 and d[i] <= 100:
#         selling = m[i] - (m[i]*(d[i]/100))
#         print(int(selling))
#     else:
#         print("Invalid Discount")

# ==========================

# A supermarket has 3 rows and 4 products in each row.
# Store the MRP in a 2D array.
# Take the discount for each product and calculate the selling price.
# Display the selling price in matrix format.


# m = list(map(int, input().split()))
# d = list(map(int, input().split()))

# k = 0
# newArr = [[0 for _ in range(4)] for _ in range(3)]
# for i in range(3):
#     for j in range(4):
#         selling = m[k] - (m[k]*(d[k]/100))
#         k+=1
#         newArr[i][j]= selling
# print(newArr)

# =======================
# Write a Python program to take Cost Price (C.P.) and Selling Price (S.P.) as input.

# If S.P. is greater than C.P., calculate and print Profit Percentage.
# Otherwise, print "Invalid".

# c = int(input())
# s = int(input())
# if s > c:
#     p = s - c 
#     print(round((p/c)*100))
# else:
#     print("Invalid")

# ===========================
# A shopkeeper has information about 5 products.
# For each product, take C.P. and S.P. as input.
# If S.P. is greater than C.P., calculate Profit Percentage.
# Otherwise, print "Invalid".
# Condition: Do not use a loop.

# c = list(map(int, input().split()))
# s = list(map(int, input().split()))
# if len(s) > 0 and s[0] > c[0]:
#     p = s[0] - c[0] 
#     print(round((p/c[0])*100))

# if len(s) > 1 and s[1] > c[1]:
#     p = s[1] - c[1] 
#     print(round((p/c[1])*100))

# if len(s) > 2 and s[2] > c[2]:
#     p = s[2] - c[2] 
#     print(round((p/c[2])*100))

# if len(s) > 3 and s[3] > c[3]:
#     p = s[3] - c[3] 
#     print(round((p/c[3])*100))

# if len(s) > 4 and s[4] > c[4]:
#     p = s[4] - c[4] 
#     print(round((p/c[4])*100))

# else:
#     print("invalid") 

# ==================

# Write a Python program that takes C.P. and S.P. for 5 products using a loop.
# For every product:
# Check whether S.P. is greater than C.P.
# If yes, calculate Profit Percentage.
# Otherwise, print "Invalid".
# Condition: Use only one loop.

# c = list(map(int, input().split()))
# s = list(map(int, input().split()))
# for i in range(len(c)):
#     if s[i] > c[i]:
#         p = s[i] - c[i] 
#         print(round((p/c[i])*100))
#     else:
#         print("invalid")

# ==========================
# https://leetcode.com/problems/running-sum-of-1d-array/?utm_source=chatgpt.com
# 1480. Running Sum of 1d Array
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         prefix = []
#         total = 0
#         for i in nums:
#             total+=i
#             prefix.append(total)
#         return prefix
# ==================================