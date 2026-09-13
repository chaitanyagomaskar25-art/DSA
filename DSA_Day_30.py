# Q1: Class Attendance Checker
# Given how many days a student was present out of total class days, calculate their attendance percentage and say if they're "Eligible" for exams (75% or more) or "Not Eligible".

# INPUT: present=70, total=90
# OUTPUT: (77.78, "Eligible")


# present  = int(input("Enter present days: "))
# total  = int(input("Enter total days: "))

# percent = round((present/total) * 100)

# if percent > 75:
#     print(percent, "Eligible")
# else:
#     print(percent, "Not Eligible")


# ======================================


# Q2: Bulk Order Discount Calculator
# Add up a shopping cart's prices, then apply a discount: 15% off if there are 5+ items AND the total is ₹2000+, otherwise 10% off if there are at least 3 items, otherwise no discount.

# INPUT: [500, 600, 700, 300, 400]
# OUTPUT: 2125.0

# a = list(map(int, input().split()))
# n = len(a)

# total = sum(a)

# if n >= 5:
#     print(total - (total*0.15))
# elif n >=3:
#     print(total - (total *0.10))
# else:
#     print(total)

# ==========================================

# Q3: Saddle Point Finder 🎯
# Find all "saddle points" in a matrix — a cell that is the smallest value in its row AND the largest value in its column at the same time. Without using min() or max().

# INPUT: 
# [[3, 7, 8],
#  [9, 11, 12],
#  [4, 6, 8]]

