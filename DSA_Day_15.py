# Ques1: Write a Python program that takes a number n and prints a square pattern of * with n rows and n columns.

# Input: 4
# Output:
# ****
# ****
# ****
# ****

# n = int(input())
# for i in range(n):
#     ans = ""
#     for j in range(n):
#         ans+="*"
#     print(ans)


# =================================
# Ques2: Write a Python program that takes a number n and prints a right-angled triangle pattern.

# Input: 5
# Output:
# *
# **
# ***
# ****
# *****

# n = int(input())
# for i in range(1,n+1):
#     ans = ""
#     for j in range(i):
#         ans+="*"
#     print(ans)

# ===============================

# Ques3: Write a Python program that takes a number n and prints the following number pattern using nested loops.

# Input: 5
# Output:
# 1
# 12
# 123
# 1234
# 12345

# n = int(input())

# for i in range(1, n+1):
#     ans = ""
#     for j in range(1,i+1):
#         ans+=f"{j}"
#     print(ans)

# ========================
# https://leetcode.com/problems/maximum-average-subarray-i/?utm_source=chatgpt.com

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         s = 0
#         m= float("-inf")
#         for i in range(len(nums)):
#             s+=nums[i]
#             if i >= k-1:
#                 a = s/k
#                 m = max(a,m)
#                 s-=nums[i-k+1]
        # return m