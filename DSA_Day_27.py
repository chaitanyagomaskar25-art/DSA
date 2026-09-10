# https://www.codechef.com/problems/ADDIS?tab=statement
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     freq = {} 
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
    
#     m = 0
#     for i in freq:
#         if freq[i] > m:
#             m = freq[i]
    
#     total = (m+1)//2
    
#     print(total)


# ===================================

# Q1: Get Value with a Default (Safe Lookup)
# Write a function that safely looks up a key in a dictionary. If the key doesn't exist, return a default value instead of causing an error.

# Input: {"a":1,"b":2}, key="c", default="Not Found"
# Output: "Not Found"

# n = int(input())
# d = {}
# for i in range(n):
#     key = input()
#     value = int(input())
#     d[key] = value

# key = input("Enter the default key: ")
# if key in d:
#     print("Found")
# else:
#     print("Not Found")

# =============================================

# Q2: Ticket Price by Age Bracket
# A theme park charges different prices based on age: under 5 → free, 5–11 → ₹100, 12–59 → ₹200, 60+ → ₹120 (senior discount).

# Input: 8
# Output: 100

# a = int(input("Enter a age: "))
# if a < 5:
#     print("Free")
# elif a <= 11:
#     print("$100")
# elif a < 60:
#     print("$200")
# else:
#     print("$120")


# =================================
# Q3: First Non-Repeating Character 🔤
# Given a string, find the first character that doesn't repeat anywhere else in it. If every character repeats, return None.

# Input: "swiss"
# Output: "w"

# s = input("Enter a string: ")
# freq = {}
# for i in s:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1

# for i in freq:
#     if freq[i] == 1:
#         print(i)
#         break
# else:
#     print("There is no non repeating character.")

# ==========================================================
# Q4: Subarray Sum Equals K 🧮
# Given an array and a target sum k, count how many contiguous subarrays sum up to exactly k.

# Input: [1, 1, 1], k=2
# Output: 2
# (subarrays [1,1] at index 0-1, and [1,1] at index 1-2 both sum to 2)

