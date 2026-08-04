# Aug 4 2026
#  Question 1 
# 3
# 3 6 - yes
# 4 14 - yes
# 9 10 - no
# t = int(input())

# for _ in range(t):
#     a,b = map(int, input().split())
#     diff = b-a
#     if diff ==0 or a<= diff:
#         print("yes")
#     else:
#         print("no")
# ========================
#  
# Question 2
# 5
# 3 2 - 2
# 5 3 -  6
# 16 18 -  72 
# 11 8 - 24
# 8 6 - 12

# import math

# t = int(input())

# for _ in range(t):
#     n,a = map(int, input().split())
#     ans = math.isqrt(n) *a
#     print(int(ans))

# ===========
# Question 3 (rating 1191)
# 6
# 1 0 2 3 0 4 - 2

# t = int(input())
# a = list(map(int, input().split()))
# n = len(a)
# c = 0
# maxC = 0

# for i in a:
#     if i !=0:
#         c +=1
#         if c > maxC:
#             maxC = c
#     else:
#         c = 0
# print(maxC)