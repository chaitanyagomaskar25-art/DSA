# Q1: Sentence Counter ✍️
# Count how many sentences are in a paragraph by counting [., !, and ?]

# Input: "Hello! How are you? I am fine."
# Output: 3

# a = input()
# c = 0
# for i in a:
#     if i in ".!?":
#         c+=1
# print(c)


# ======================================

# Return all requests whose status is "Failed".
# Input
# [
# { id:1, status:"Success"},
# { id:2, status:"Failed"},
# { id:3, status:"Success"},
# { id:4, status:"Failed"}
# ]
# Expected Output
# [
# { id:2, status:"Failed"},
# { id:4, status:"Failed"}
# ]

# n = int(input())
# a = []
# for i in range(n):
#     id = int(input(f"Enter id of {i+1} person: "))
#     status = input(f"Enter status of {i+1} person: ")
#     a.append({'id':id, 'status': status})
# result = []
# for i in a:
#     if 'status' in i and i["status"].lower() == "failed":
#         result.append(i)
# print(result)

# ========================================
# Each authentication token contains an expiry timestamp.
# Return all expired tokens.
# Input
# const currentTime = 1000;

# [
# {id:1,expires:900},
# {id:2,expires:1200},
# {id:3,expires:800}
# ]
# Expected Output
# [
# {id:1,expires:900},
# {id:3,expires:800}
# ]

# t = int(input("Enter currentTime: "))

# n = int(input())
# a = []
# for i in range(n):
#     id = int(input(f"Enter id of {i+1} person: "))
#     expires = int(input(f"Enter expires of {i+1} person: "))
#     a.append({'id':id, 'expires': expires})
    
# result = []

# for i in a:
#     if i['expires'] < t:
#         result.append(i)

# print(result)

# ==========================

# Each notification belongs to a user.
# Count how many notifications each user received.
# Input
# [
# "Rinki",
# "Amit",
# "Rinki",
# "Neha",
# "Rinki"
# ]
# Expected Output
# {
# Rinki:3,
# Amit:1,
# Neha:1
# }

# a = list(map(str, input().split()))
# result = {}
# for i in a:
#     if i.lower() in result:
#         result[i.lower()]+=1
#     else:
#         result[i.lower()] = 1
# print(result)


# ==================================
