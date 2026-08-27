# Given an array of integers, count how many times each element appears in the array.
# You should print each unique element along with its frequency.
# The order of the elements in the output can be the order in which they first appear in the array.

# INPUT 2 3 2 4 3 2 5 4
# OUTPUT 
# 2: 3
# 3: 2
# 4: 2
# 5: 1 

# a = list(map(int, input().split()))
# freq = {}
# for i in a:
#     if i not in freq:
#         freq[i] = 1
#     else:
#         freq[i]+=1
        
# print(freq)

# =========================================

# given an array of integers and a target value K, find all pairs of elements whose sum is equal to K.
# Each pair should contain two different elements from the array.
# For this problem, consider the values, not the indices.If duplicate values can create multiple identical pairs, print the pair only once.Print each pair in increasing order.

# input 2 7 4 5 3 8
#  K=10

# output 
# 2 8
# 3 7

# input -5 -2 0 3 5 7 10
# k= 5
# output 
# -5 10
# -2 7
# 0 5

# a = list(map(int, input().split()))
# k = int(input())
# freq = []
# for i in a:
#     for j in a:
#         if i + j == k and i!=j:
#             freq.append((i,j))
# # print(freq[:len(freq)//2])
# for i in range(len(freq)//2):
#     print(freq[i])


# ==========================================
# Given an array of integers and an integer K, find the length of the longest contiguous subarray whose sum is exactly equal to K.
# A subarray must contain continuous elements from the original array.You only need to output the maximum length.If no subarray has a sum equal to K, output 0.

# input 10 5 2 7 1 9
# k=15

# output 4
# a = list(map(int, input().split()))
# t = int(input())
# m = 0
# for i in range(len(a)):
#     s = a[i]
#     c = 1
#     for j in range(i+1, len(a)):
#         s+=a[j]
#         c+=1
#         if s == t:
#             if c > m:
#                 m = c
#         if s > t:
#             break     
# print(m) 


# ============================================

# Q1:  Insurance Premium Calculator 🏥
# Calculate insurance premium: base rate depends on age (<25→₹3000, 25-44→₹5000, 45-59→₹8000, 60+→₹12000). 
# Add 30% if the person has a pre-existing disease, and another 20% if they smoke (both can apply together). 

# INPUT: age=65, has_disease=True, smoker=True 
# OUTPUT: 18720.0 

# a = int(input())
# d = bool(input())
# s = bool(input())
# total = 0
# if a < 25:
#     total+=3000 
# elif a < 44:
#     total+=5000
# elif a<59:
#     total+=8000
# else:
#     total+=12000

# if d:
#     total+=total*3/10
# if s:
#     total+=total*2/10

# print(total)

# ===================================

# Q2: Move Zeros to End 0️⃣
# Move all zeros in an array to the end, while keeping the relative order of non-zero elements.

# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

# a = list(map(int, input().split()))
# s = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         a[s], a[i] = a[i], a[s]
#         s+=1
        
# print(a)

# =======================================

# Q3: Identity Matrix Checker ➕
# Check if a given square matrix is an identity matrix (1s on the diagonal, 0s everywhere else).

# Input: [[1,0,0],[0,1,0],[0,0,1]]
# Output: True

# n = int(input())
# a = [list(map(int, input().split())) for i in range(n)]
# for i in range(n):
#     j = i
#     if a[i][j] != 1:
#         print(False)
#         break
# else:
#     print(True)

# ====================================

# Q4: String Compression 🗜️
# Compress a string by counting consecutive repeated characters: "aaabbc" → "a3b2c1". 

# Input: "aaabbc"
# Output: "a3b2c1"

# s = input()
# f = {}
# for i in s:
#     if i not in f:
#         f[i] = 1
#     else:
#         f[i]+=1

# newS = ""
# for key, value in f.items():
#     newS+= str(key)+str(value)
# print(newS)

# ========================
