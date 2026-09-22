# Q1 — Odd-Even Treasure Hunt

# A treasure map contains a sequence of numbers:

# numbers = [14, 7, 22, 9, 31, 16, 5, 28]

# The treasure hunter follows these rules:

# 1. Add all the even numbers.
# 2. Add all the odd numbers.
# 3. Calculate the difference between the two totals.
# 4. Print which total is larger: "Even" or "Odd".

# Expected output:

# Even Total: 80
# Odd Total: 52
# Difference: 28
# Larger Total: Even

# a = list(map(int, input().split()))
# o = 0
# e = 0
# for i in a:
#     if i % 2 == 0:
#         e+=i
#     else:
#         o+=i

# print(f'Even Total : {e}\nOdd Total : {o}\nDifference : {abs(e-o)}')
# if e > o:
#     print("EVEN")
# else:
#     print("ODD")


# ==========================

# Q2 — Username Cleaner

# A website receives usernames with unnecessary spaces and mixed capitalization:

# usernames = ["  Nitin ", "RAHUL  ", "  priya", "Amit ", "  Kiran  "]


# Create a cleaned version of each username by:

# 1. Removing spaces from the beginning and end.
# 2. Converting the username so that the first letter is uppercase and the remaining letters are lowercase.
# 3. Print each cleaned username.
# 4. Count how many usernames contain the letter i.

# Expected output:

# Nitin
# Rahul
# Priya
# Amit
# Kiran

# Users containing i: 4

# a = list(map(str, input().split()))
# c=0
# for i in range(len(a)):
#     if "i" in a[i]:
#         c+=1
#     b = a[i].strip()
#     print(b[0].upper()+b[1:].lower())

# print(f"Users containing i : {c}")


# ===========================================

# Q3 — Mini ATM Transaction Tracker

# A bank account starts with:

# balance = 5000

# The following transactions occur:

# transactions = [1200, -500, 800, -2000, 1500, -700]

# Rules:

# 1. A positive number means money was deposited.
# 2. A negative number means money was withdrawn.
# 3. Process the transactions one by one.
# 4. Print the balance after every transaction.
# 5. Find the largest deposit.
# 6. Find the largest withdrawal.
# 7. At the end, print the final balance.
# 8. If the balance ever goes below 1000, print "Warning: Low Balance".

# Expected output:

# After transaction 1: 6200
# After transaction 2: 5700
# After transaction 3: 6500
# After transaction 4: 4500
# After transaction 5: 6000
# After transaction 6: 5300

# Largest Deposit: 1500
# Largest Withdrawal: 2000
# Final Balance: 5300

# ld = 0
# lw = float("inf")
# f = 5000
# a = list(map(int, input().split()))

# for i in range(len(a)):
#     f+=a[i]
#     print(f"After transaction {i+1} : {f}")
#     if a[i] > 0 and a[i] > ld:
#         ld = a[i]
#     if a[i] < 0 and a[i] < lw:
#         lw = a[i]

# print(f"Largest Deposit : {ld}\nLargest Withdrawal : {abs(lw)}\nFinal Balance : {f}")

# ====================================

