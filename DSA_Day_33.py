# Q1: Cricket Scorecard 
# Given a list containing runs scored in each ball.
# Rules:
# Count number of boundaries (4s and 6s)
# Count dot balls (0)
# Calculate total score

# INPUT: [1, 4, 0, 2, 6, 1, 0, 4]
# OUTPUT:       Total Score: 18
#                        Boundaries: 3
#                        Dot Balls: 2


# a = list(map(int, input().split()))
# t = 0
# b = 0
# d = 0
# for i in a:
#     t+=i
#     if i == 4 or i == 6:
#         b+=1
#     elif i == 0:
#         d +=1
        
# print(f" Total Score: {t}\n Bounderies: {b} \n Dot Balls: {d}")

# =====================================

# Q2: Sum of Digits 🧮
# Extract and add up every digit of a number using only math — no string conversion allowed.

# Input: 1234
# Output: 10

# n = int(input())
# s = 0
# while n > 0:
#     d = n % 10
#     s += d
#     n = n //10
    
# print(s)

# ============================================

# Q3: All Pairs Summing to Target 🎯 
# Given a list of numbers and a target value, find all pairs of indices (i, j) where the two numbers add up to the target. Each number can only be used once per pair (don't reuse the same index in two different pairs).

# INPUT: arr = [2, 7, 11, 15, 5, 9] , target = 9
# OUTPUT: [(0, 1)]

# a = list(map(int, input().split()))
# t = int(input())

# result = []

# for i in range(len(a)):
#     for j in range(len(a)):
#         s = a[i]+a[j]
#         pair = sorted((i, j))
#         if s == t and pair not in result:
#             result.append(pair)

# print(result)

# ===========================

# Ques1: Dictionary Inversion 🔄
# Flip a dictionary so that keys become values and values become keys.

# Input: {"a":1, "b":2, "c":3}
# Output: {1:"a", 2:"b", 3:"c"}

# a = {"a":1, "b":2, "c":3}
# b = {}
# for keys, values in a.items():
#     b[values] = keys

# print(b)

# ======================================================================

# Ques2: Running Average of a List 📊
# A sensor records values one by one. After each new value, print the average of everything seen so far (running average).

# Input: [4, 7, 13, 2, 1]
# Output: [4.0, 5.5, 8.0, 6.5, 5.4]

# a = list(map(int, input().split()))
# result = []
# for i in range(len(a)):
#     total = sum(a[:i+1])
#     avg = total / (i+1)
#     result.append(avg)

# print(result)

# ============================================================

# Ques3: Matrix Row Sums and Column Sums 🔲
# Given a 2D matrix, compute the sum of each row and the sum of each column, returning both as separate lists.

# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: Row sums: [6,15,24] | Col sums: [12,15,18]

# a = [[1,2,3],[4,5,6],[7,8,9]]

# rows = [sum(r) for r in a]
# cols = [sum(c) for c in zip(*a)]
# print(rows, cols)


# ===============================
