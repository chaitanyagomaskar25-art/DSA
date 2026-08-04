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


# "Write a program to check 
# n = int(input())
# if n%5==0 and n% 11 ==0:
#     print("both")
# elif n%5 ==0:
#     print("5")
# elif n%11 ==0:
#     print("11")
# else:
#     print("none")

# Input four sides and an angle of n 
# a,b,c,d, angle = map(int, input().split())
# if a == b== c == d:
#     if angle == 90:
#         print("Suqare")
#     else:
#         print("Rhombus")
# elif a == c and b == d:
#     if angle == 90:
#         print("Rectangle")
#     else:
#         print("Parallelogram")
# else:
#     print("Irregular Quadrilateral")


# A certain steel is graded 
# r, c, t = map(int, input().split())
# if r > 50:
#     if c > 0.7:
#         if t > 5600:
#             print("Grade 10")
#         else:
#             print("Grade 9")
#     else:
#         if t > 5600:
#             print("Grade 7")
#         else:
#             print("Grade 0")
# else:
#     if c > 0.7 :
#         if t > 5600:
#             print("Grade 8")
#         else:
#             print("Grade 0")
#     else:
#         print("Grade 0")

# A company has N employees. Each employee has completed a certain number of tasks.
# n = list(map(int, input().split()))
# newArr = []
# for i in n:
#     if i >= 50 and i %2 ==0:
#         newArr.append(i)
#         print(i)
# print(newArr)

