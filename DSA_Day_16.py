# 1. Find User with Highest Balance
# You are given an array of user records stored in memory.
# const users = [
#   { id: 1, name: "Rinki", balance: 4500 },
#   { id: 2, name: "Amit", balance: 12000 },
#   { id: 3, name: "Neha", balance: 8000 }
# ];
# Find the user who has the highest account balance.
# Expected Output
# Amit - ₹12000

# users = []
# n = int(input("Enter the number of users: "))
# for i in range(n):
#     n = input(f"Enter the name of {i+1} user: ")
#     b = int(input(f"Enter the balance of {i+1} user: "))
#     users.append({"id": i+1, "name": n, "balance": b})

# m = 0
# u = ""
# for i in users:
#     if i["balance"] > m:
#         m = i["balance"]
#         u = i["name"]
# print(f"{u} - {m}")
    
# ======================================
# 2. Merge Two Database Tables
# You have two collections.
# Users
# [
#   { id: 1, name: "Rinki" },
#   { id: 2, name: "Amit" }
# ]
# Orders
# [
#   { userId: 1, product: "Laptop" },
#   { userId: 2, product: "Mouse" },
#   { userId: 1, product: "Keyboard" }
# ]
# Merge them so each order also contains the user's name.
# Expected Output
# [
#   { name: "Rinki", product: "Laptop" },
#   { name: "Amit", product: "Mouse" },
#   { name: "Rinki", product: "Keyboard" }
# ]

# n = int(input("Enter the number of users: "))
# users = []
# orders = []
# for i in range(n):
#     n = input(f"Enter the name of user {i+1} : ")
#     users.append({"id": i+1, "name": n})

# m = int(input("Enter the number of orders of users: "))
# for i in range(m):
#     userId = int(input("Enter te user ID: "))
#     p = input(f"Enter the product for the user of id {userId}: ")
#     orders.append({"userId": userId, "product": p})

# newArr = []
# for order in orders:
#     for user in users:
#         if user["id"] == order["userId"]:
#             newArr.append({
#                 "name": user["name"],
#                 "product": order["product"]
#             })

# print(newArr)

# ===================================

# 3. Find Missing User IDs
# Database IDs should be continuous.
# Current IDs:
# [1, 2, 3, 5, 6, 8]
# Find all missing IDs.
# Expected Output
# [4, 7]

# a = list(map(int, input().split()))
# m = [i for i in range(1, max(a)+1)]
# missing = []
# for j in m:
#     if j not in a:
#         missing.append(j)
# # missing = [i for i in m if i not in a]
# print(missing)

# ===========================================
