# https://leetcode.com/problems/range-sum-query-immutable/description/?utm_source=chatgpt.com

# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.prefix = []
#         total = 0
#         for i in nums:
#             total+=i
#             self.prefix.append(total)
#     def sumRange(self, left: int, right: int) -> int:
#         if left == 0:
#             return self.prefix[right]
#         else:
#             return self.prefix[right] - self.prefix[left-1]

# ==============================
# https://leetcode.com/problems/find-pivot-index/description/?utm_source=chatgpt.com

# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         prefix = []
#         total = 0
#         for i in nums:
#             total += i
#             prefix.append(total)
#         n = len(nums)
#         sum1 = 0
#         for i in range(n):
#             sumB = prefix[i]
#             sumA = prefix[n-1] - prefix[i-1]
#             if i == 0:
#                 sumB = 0
#                 sumA = prefix[n-1] - nums[i]
#             if sumB - sumA == 0:
#                 return i
#         else:
#             return -1

# ======================
# https://leetcode.com/problems/find-the-highest-altitude/description/?utm_source=chatgpt.com

# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#         prefix = [0]
#         total = 0
#         for i in gain:
#             total += i
#             prefix.append(total)
#         return max(prefix)
# =================================

# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/PETSTORE?tab=statement
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
   
#     if n%2!=0:
#         print("no")
#         continue
#     a.sort()
#     pos = True
#     for i in range(0, n, 2):
#         if a[i]!=a[i+1]:
#             pos = False
#             break
#     if pos:
#         print("yes")
#     else:
#         print("no")


# ================================