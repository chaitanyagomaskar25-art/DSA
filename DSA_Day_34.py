# Q1: Count Positives, Negatives, Zeros 🔢
# Given a list of numbers, count how many are positive, negative, and exactly zero.

# Input: [1,-2,0,3,-4,0,5]
# Output: (3, 2, 2)

# a = list(map(int, input().split()))

# p = 0
# n = 0
# z =0
# for i in a:
#     if i == 0:
#         z+=1
#     elif i > 0:
#         p+=1
#     else:
#         n+=1
# print((p,n,z))


# ==================================

# Q2: Dictionary Inversion 🔄
# Flip a dictionary so that keys become values and values become keys.

# Input: {"a":1, "b":2, "c":3}
# Output: {1:"a", 2:"b", 3:"c"}
# a = {"a":1, "b":2, "c":3}
# newDict = {}
# for keys, values in a.items():
#     newDict[values] = keys
# print(newDict)


# ==========================

# Q3: Smart Title Case Converter 🔤
# Convert a sentence to title case, but keep "small words" like the, in, on, and, but, or lowercase — unless they're the first word.

# Input: "the quick brown fox and the lazy dog"
# Output: "The Quick Brown Fox and the Lazy Dog"
# a = input()
# arr = a.split()
# exception  = ["the", "in", "on", "and", "but", "or"]

# for i in range(len(arr)):
#     if arr[i] in exception and i == 0:
#         arr[i] = arr[i][0].upper()+arr[i][1:]
#     if arr[i] not in exception:
#         arr[i] = arr[i][0].upper()+arr[i][1:]
# print(" ".join(arr))

# ======================

# Ques4: Find All Duplicate Values in a Matrix 🔍
# Scan every cell of a matrix and find all values that appear more than once — reporting all their positions.

# Input: [[1,2,3],[4,2,6],[7,8,1]]
# Output: {1: [(0,0),(2,2)], 2: [(0,1),(1,1)]}

# a = [[1,2,3],[4,2,6],[7,8,1]]
# result = {}
# for i in range(len(a)):
#     for j in range((len(a[i]))):
#         val = a[i][j]
#         if val in result:
#             result[val].append((i, j))
#         else:
#             result[val] = [(i,j)]
# final = {}
# for i in result:
#     if (len(result[i])) > 1:
#         final[i] = result[i]
# print(final)

# ====================================
# Q1: Flatten a Nested List 📋
# Given a list of lists (one level deep), flatten it into a single list containing all elements in order. 

# Input: [[1,2],[3,4],[5,6]]
# Output: [1,2,3,4,5,6]

# a = [[1,2],[3,4],[5,6]]
# b =[]
# for i in range(len(a)):
#     b.extend(a[i])
# print(b)

# ==================================
