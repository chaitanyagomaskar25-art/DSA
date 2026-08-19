# Take age, gender, and working days of a worker. Calculate wages based on the given wage/day rules. If age is not between 18–40, print Enter appropriate age.   if male per day = 700 if female per day = 750

# a = int(input())
# g = input()
# d = int(input())
# if a > 18 and a < 40:
#     if g.lower() == "male":
#         total = 700*d
#     else:
#         total = 750&d
#     print(total)
# else:
#     print("Invalid age")

# ========================================

# Using a single loop, take age, gender, and working days of 5 workers and calculate their wages.
# t = int(input())
# for _ in range(t):
#     a , d = map(int, input().spllit())
#     g = input()
#     if a > 18 and a < 40:
#         if g.lower() == "male":
#             total = 700*d
#         else:
#             total = 750&d
#         print(total)
#     else:
#         print("Invalid age")

# ===========================================
# Using a nested loop, take details of 3 departments, with 3 workers in each department, and calculate the wages of every worker.

# d = int(input("Enter Department No.: "))
# for _ in range(d):
#     w = int(input("Enter Workers number in that department: "))
#     for _ in range(w):
#         a , d = map(int, input("Enter age and no. of working days of worker: ").split())
#         g = input("Enter gender of that worker: ")
#         if a > 18 and a < 40:
#             if g.lower() == "male":
#                 total = 700*d
#             else:
#                 total = 750&d
#             print(total)
#         else:
#             print("Invalid age")

# ========================================

# A company has 2 branches, each branch has 2 departments, and each department has 3 workers. Take the age, gender, and working days of every worker and calculate their wages.
# Input:

# Branch 1:
# Department 1 → [20, "M", 10], [25, "F", 10], [30, "M", 10]
# Department 2 → [35, "F", 10], [22, "M", 5], [40, "F", 6]

# Branch 2:
# Department 1 → [28, "F", 7], [32, "M", 9], [17, "M", 10]
# Department 2 → [19, "F", 6], [31, "M", 10], [26, "M", 7]

# Constraint: Use three nested loops.


# b = int(input("Enter No. of branches"))
# for _ in range(b):
#     d = int(input("Enter No. Departments in each branch: "))
#     for _ in range(d):
#         w = int(input("Enter Workers number in that department: "))
#         for _ in range(w):
#             a , d = map(int, input("Enter age and no. of working days of worker: ").split())
#             g = input("Enter gender of that worker: ")
#             if a > 18 and a < 40:
#                 if g.lower() == "male":
#                     total = 700*d
#                 else:
#                     total = 750&d
#                 print(total)
#             else:
#                 print("Invalid age")

# ====================================================

# Given three 1D arrays containing age, gender, and working days of 5 workers, calculate the wage of each worker.
# age = [20, 25, 30, 40, 17]
# gender = ["M", "F", "M", "F", "M"]
# days = [10, 10, 10, 10, 10]
# Constraint: Use loops. Do not create separate wage values manually.

# n = int(input())
# age = list(map(int, input(f"Enter the age of {n} workers: ").split()))
# gender = list(map(str, input(f"Enter the gender of {n} workers: ").split()))
# days = list(map(int, input(f"Enter the days of {n} workers: ").split()))

# for i in range(n):
#     if age[i] > 18 and age[i] < 40:
#         if gender[i].lower() == "male":
#             total = 700*days[i]
#         else:
#             total = 750&days[i]
#         print(total, end=" , ")
#     else:
#         print("Invalid age")

# =======================================

# d = int(input("Enter Department No.: "))
# arr = [[] for _ in range(d)]
# print(arr)
# for i in range(d):
#     w = int(input("Enter Workers number in that department: "))
#     for j in range(w):
#         a , d = map(int, input("Enter age and no. of working days of worker: ").split())
#         g = input("Enter gender of that worker: ")
#         arr[i].append([a, d, g])
#         if a > 18 and a < 40:
#             if g.lower() == "male":
#                 total = 700*d
#             else:
#                 total = 750&d
#             print(total)
#         else:
#             print("Invalid age")
# print(arr)


# ================================================
# Ques1: Support Ticket Escalation 🎫
# A helpdesk logs ticket statuses for a day as a list: "Open", "Resolved", "Escalated". If 2 tickets get escalated consecutively, management wants an alert with the index where it first happened. If it never happens, print "No Escalation Pattern".

# Input: ["Open", "Resolved", "Escalated", "Open", "Escalated", "Escalated", "Resolved"]
# Output: Alert triggered at index 5

# a = list(map(str, input().split()))
# c = 0
# for i in range(len(a)):
#     if a[i].lower() == "escalated":
#         c+=1
#     else: 
#         c = 0
#     if c>=2:
#         print(f" Alert triggered at index {i}")
#         break
# else:
#     print("No Escalation Pattern")
    
    
# ==========================================
# Ques2 : Stock Price Drop Alert 📉
# A stock's closing price is recorded daily. Find the maximum single-day drop — i.e., the biggest decrease from one day to the very next day. Print the drop amount and the day index where it happened.

# Input: [100, 105, 95, 130, 90, 110]
# Output: Max drop = 40 on day index 3 to 4
# (130 → 90 is a drop of 40, the biggest single-day fall)

# a = list(map(int, input().split()))
# max = 0
# diff = 0
# ind = 0
# for i in range(len(a)-1):
#     if a[i] > a[i+1]:
#         diff = a[i]-a[i+1]
#     if diff > max:
#         max = diff
#         ind = i
# print(f" Max drop = {max} on day index {ind} to {ind+1}")


# ===================================
