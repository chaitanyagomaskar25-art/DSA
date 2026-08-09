# Equalize AB (1069)
# t = int(input())

# for _ in range(t):
#     a,b,c = map(int, input().split())
#     diff = a-b
#     if diff%(2*c)==0:
#         print("yes")
#     else:
#         print("no")
# =============================
# Counting Problem (1065)
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
    
#     if sum(a) %2==0 and [n for n in a if n%2!=0]:
#         print("yes")
#     else:
#         print("no")
# =======================

# A company has N employees. Each employee has completed a certain number of tasks.

# An employee is eligible for a bonus if:
# Tasks completed ≥ 50
# AND tasks completed is an even number.
# Print the number of eligible employees.

# a = list(map(int, input().split()))
# for i in a:
#     if i >= 50 and i%2==0:
#         print(i)

# ====================

# Now store the task counts of only the eligible employees in a new array.
# Print the new array.

# a = list(map(int, input().split()))
# newArr = []
# for i in a:
#     if i >= 50 and i%2==0:
#         newArr.append(i)
# print(newArr)

# =================

# The company wants to reward the top performer among the eligible employees.
# Find:
# Highest task count
# Second highest task count

# a = list(map(int, input().split()))
# newArr = []
# for i in a:
#     if i >= 50 and i%2==0:
#         newArr.append(i)
# print(newArr)

# maxp = 0
# secmaxp = newArr[0]
# for j in newArr:
#     if j > maxp:
#         maxp = j
#     if j > secmaxp and j != maxp:
#         secmaxp = j
# print(maxp, secmaxp)

# =======================

# Employees are promoted if:
# They are eligible for a bonus 
# AND their task count is at least 90% of the highest task count.
# Print the promoted employees.

# a = list(map(int, input().split()))
# newArr = []
# for i in a:
#     if i >= 50 and i%2==0:
#         newArr.append(i)

# maxp = 0
# for j in newArr:
#     if j > maxp:
#         maxp = j
# bonus = maxp*90/100
# b = [n for n in newArr if n >= bonus]
# print(b)

# ============================
# Problem 4: Best Parking Location
# If there are multiple locations where the bus can park, choose the parking block that lies in the middle among all the valid parking locations.
# If the number of valid parking locations is odd, choose the exact middle one.
# If the number of valid parking locations is even, choose the left-middle parking location.
# Print the starting index of the selected parking block.
# Input: Parking Slots: 0 0 0 1 0 0 0 1 0 0 0
# Output: 5

