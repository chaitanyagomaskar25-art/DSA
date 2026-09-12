# You are given an array of N non-negative integers, where each element represents the height of a vertical bar. All bars have a width of 1 unit.

# When it rains, water can be trapped between these bars. Your task is to calculate the total amount of rainwater that can be trapped after raining.

# A bar can trap water only when there are taller bars on both its left and right sides.

# Input Format
# The first line contains an integer N, representing the number of bars.
# The second line contains N space-separated integers representing the heights of the bars.
# Output Format

# Print a single integer representing the total amount of rainwater trapped.

# Input
# 6
# 4 2 0 3 2 5
# Output
# 9

# Input

# 5
# 5 4 3 2 1

# Output

# 0

# Input

# 5
# 0 0 0 0 0

# Output

# 0

# n = int(input())
# a = list(map(int, input().split()))
# total = 0
# for i in range(n):
#     leftMax = max(a[:i+1])
#     rightMax = max(a[i:])
#     total+=min(leftMax, rightMax) - a[i]
# print(total)


# ===================================

# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         c = 0
#         for i in nums:
#             if len(str(i)) % 2 == 0:
#                 c+=1
#         return c


# ==========================================

