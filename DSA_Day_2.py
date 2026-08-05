# Problem 1
# A student qualifies if
# Marks ≥ 75
# Attendance ≥ 85
# No backlog
# Count qualified students.

# m = list(map(int, input().split(" ")))
# a = list(map(int, input().split(" ")))
# isBacklog = list(map(bool, input().split(" ")))
# c = 0
# n = len(m)
# for i in range(n):
#     if m[i] >= 75 and a[i] >= 85 and isBacklog[i] == True:
#         c +=1
# print(c)


# =================
# Problem 2
# Store qualified students' marks.
# Find
# Highest
# Lowest
# Average

# m = list(map(int, input().split(" ")))
# a = list(map(int, input().split(" ")))
# isBacklog = list(map(bool, input().split(" ")))
# n = len(m)
# qualifiedStudent = []
# for i in range(n):
#     if m[i] >= 75 and a[i] >= 85 and isBacklog[i] == True:   
#         qualifiedStudent.append(m[i])
    
# print(qualifiedStudent)
# print(max(m))
# print(min(m))
# print(sum(m)/n)

# ==================

# Problem 3
# Scholarship Rules
# Gold: Marks ≥ Highest − 5
# Silver: Marks ≥ Average
# Bronze: Remaining qualified students
# Print all three categories separately.


# m = list(map(int, input().split(" ")))
# a = list(map(int, input().split(" ")))
# isBacklog = list(map(bool, input().split(" ")))
# n = len(m)
# qualifiedStudent = []
# highest = max(m)
# lowest = min(m)
# avg = sum(m) /n
# gold = []
# silver = []
# bronz = []
# for i in range(n):
#     if m[i] >= 75 and a[i] >= 85 and isBacklog[i] == True:   
#         qualifiedStudent.append(m[i])
#         if m[i] >= highest - 5:
#             gold.append(m[i])
#         elif m[i] >= avg:
#             silver.append(m[i])
#         else:
#             bronz.append(m[i])
# print(qualifiedStudent)
# print(highest, avg, lowest)
# print(gold)
# print(silver)
# print(bronz)


# =========================
# Problem 1 
# Each candidate has Aptitude Score and Technical Score
# A candidate qualifies if
# Aptitude ≥ 70 and Technical ≥ 75 and (Aptitude + Technical) ≥ 160
# Count qualified candidates.

# a = list(map(int, input().split()))
# t = list(map(int, input().split()))
# c = 0
# for i, j in zip(a, t):
#     if i >=70 and j >= 75 and (i+j) >= 160:
#         c +=1
# print(c)

# ================

#  Problem 2 
# Store only qualified candidates.
# Calculate their final score
# Final Score =
# 0.4 × Aptitude + 0.6 × Technical

# a = list(map(int, input().split()))
# t = list(map(int, input().split()))
# c = []
# for i, j in zip(a, t):
#     if i >=70 and j >= 75 and (i+j) >= 160:
#         final_Score = (0.4*i )+ (0.6 * j)
#         c.append((i,j, final_Score))
# print(c)

# ==============

# Problem 3 
# Find Highest Final Score
# Second Highest Final Score

# a = list(map(int, input().split()))
# t = list(map(int, input().split()))
# c = []
# for i, j in zip(a, t):
#     if i >=70 and j >= 75 and (i+j) >= 160:
#         final_Score = int((0.4*i )+ (0.6 * j))
#         c.append((i,j, final_Score))
# print(c)
# maxS = 0
# maxSec = 0
# for i in c:
#     if i[2] > maxS:
#         maxS = i[2]
#     if i[2] > maxSec and i[2] != maxS:
#         maxSec = i[2]
# print(maxS, maxSec)


# ==============

#  Problem 4 
# HR wants to create interview batches.
# Batch A: Top 20% scores
# Batch B: Next 30%
# Batch C: Remaining
# Print each batch.

# a = list(map(int, input().split()))
# t = list(map(int, input().split()))
# c = []
# for i, j in zip(a, t):
#     if i >=70 and j >= 75 and (i+j) >= 160:
#         final_Score = int((0.4*i )+ (0.6 * j))
#         c.append((i,j, final_Score))
# c.sort(key = lambda x: x[2], reverse=True)
# print(c)
# candidates = len(c)
# countA = int(0.2*candidates)
# countB = int(0.3*candidates)
# A = c[:countA]
# B = c[countA: countA+countB]
# C = c[countB:]
# print(A, B, C)

# ==================

# Floor and ceil in a sorted array
# class Solution:
#     def find_floor_ceil(self, arr, k):
#         # write your code here
#         l = 0
#         h = len(arr)
#         f = -1
#         c = -1
#         while l<h:
#             m = (l+h)//2
#             if arr[m] ==k:
#                 return k,k
#             elif arr[m] <k:
#                 f = arr[m]
#                 l=m+1
#             else:
#                 c = arr[m]
#                 h=m
#         return f,c
        
        
# =====================
# Find the insert position
# class Solution:
#     def search_insert_position(self, arr, target):
#         # write your code here
#         l = 0
#         h = len(arr)
#         while l<h:
#             m = (l+h)//2
#             if arr[m] < target:
#                 l=m+1
#             else:
#                 h=m
#         return l


# ==========================
# Upper Bound in a Sorted Array
# def upper_bound(nums, x):
#     # write code here...
#     l = 0
#     h = len(nums)
#     while l<h:
#         m = (l+h)//2
#         if nums[m]<=x:
#             l=m+1
#         else:
#             h=m
#     return l

# ============
# Lower Bound

# def solve(nums, x):
#     # write your logic here...
#     h = len(nums)
#     l = 0
#     while l<h:
#         m = (l+h)//2
#         if nums[m] < x:
#             l = m+1
#         else:
#             h = m
#     return l

          