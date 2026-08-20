 	
# A steel is graded according to:
# Rockwell hardness > 50
# Carbon content > 0.7
# Tensile strength > 5600 kg/cm²
# Grades:
# Grade 10: All three conditions satisfied
# Grade 9: Conditions (i) and (ii)
# Grade 8: Conditions (ii) and (iii)
# Grade 7: Conditions (i) and (iii)
# Grade 0: Otherwise

# r, t = map(int, input().split())
# c = float(input())
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
#     if c > 0.5 and t > 5600:
#         print("Grade 8")
#     else:
#         print("Grade 0")

# =====================================================
# Take the three properties of 5 steel samples using a loop and determine the grade of each sample.
# t = int(input())
# for _ in range(t):
#     r, t = map(int, input().split())
#     c = float(input())
#     if r > 50:
#         if c > 0.7:
#             if t > 5600:
#                 print("Grade 10")
#             else:
#                 print("Grade 9")
#         else:
#             if t > 5600:
#                 print("Grade 7")
#             else:
#                 print("Grade 0")
#     else:
#         if c > 0.5 and t > 5600:
#             print("Grade 8")
#         else:
#             print("Grade 0")


# ==================================
# A factory has 3 production lines, with 3 steel samples per line. Determine the grade of every sample.
# f = int(input())
# for _ in range(f):
#     s = int(input())
#     for _ in range(s):
#         r, t = map(int, input().split())
#         c = float(input())
#         if r > 50:
#             if c > 0.7:
#                 if t > 5600:
#                     print("Grade 10")
#                 else:
#                     print("Grade 9")
#             else:
#                 if t > 5600:
#                     print("Grade 7")
#                 else:
#                     print("Grade 0")
#         else:
#             if c > 0.5 and t > 5600:
#                 print("Grade 8")
#             else:
#                 print("Grade 0")

# ========================================
# Ques3 : Employee Shift Table 🕐 (Nested Loop)
# A company tracks shift hours for 3 employees over a week using a 2D list (7 days each):
# Employee 1: [8, 8, 0, 8, 8, 0, 0]
# Employee 2: [8, 8, 8, 8, 8, 8, 0]
# Employee 3: [0, 8, 8, 0, 8, 0, 0]
# Find which employee worked the most total hours, and print their name with total hours.

# t = int(input("Enter Employee no.: "))
# max = 0
# emp = 0
# for j in range(t):
#     c = 0
#     b = list(map(int, input().split()))
#     for i in b:
#         if i !=0:
#             c+=1
#         if c > max:
#             max = c 
#             emp = j
# print(f"The employee {emp+1} has highest working hours of {max}")
# ===============================

#  A cinema row has seats, marked as 1 = booked and 0 = empty in a list.
# A booked seat is called "Lonely" if the seat right next to it on both sides is empty (or doesn't exist, like at the very start/end of the row).Count how many lonely seats are in the row.
# INPUT: [0, 1, 0, 0, 1, 1, 0, 1, 0]
# OUTPUT: Lonely seats: 2

# a = list(map(int, input().split()))
# c = 0
# for i in range(1,len(a)-1):
#     if a[i-1] == 0 and a[i+1] == 0:
#         c +=1
# print(f"Lonely seats are {c}")

# ====================================

# Ques2 : Cab Surge Pricing Streak 🚕 

# A cab company logs the fare price for every ride in a day. If the fare goes above ₹150, it means "surge pricing" is active. Find the longest continuous streak of rides where surge pricing stayed active without breaking.
# INPUT: 
# Fares: [120, 160, 180, 140, 155, 170, 190, 130]
# Threshold: 150
# OUTPUT: Longest surge streak: 3

# f = list(map(int, input().split()))
# t = int(input())
# c = 0
# m = 0
# for i in f:
#     if i > t:
#         c+=1
#     else:
#         c = 0
#     if c > m:
#         m = c
# print(f"Longest surge streak: {m}")


# ============================================
