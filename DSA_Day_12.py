# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MAKEMONEY

# t = int(input())

# for _ in range(t):
#     n,x,c = map(int, input().split())
#     a = list(map(int, input().split()))
#     print(sum(max(y, x-c) for y in a))
    
    
# ========================
# https://leetcode.com/problems/remove-element/?lang=c&utm_source=chatgpt.com

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         s = 0
#         for i in range(0, len(nums)):
#             if nums[i] != val:
#                 nums[s] = nums[i]
#                 s+=1
#         return s


# =============================
# https://leetcode.com/problems/move-zeroes/?utm_source=chatgpt.com

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         s = 0
#         for f in range(len(nums)):
#             if nums[f] != 0:
#                 temp = nums[s]
#                 nums[s] = nums[f]
#                 nums[f] = temp
#                 s+=1

# ===============================
# find maximum
# a = list(map(int, input().split()))
# m = 0
# for i in a:
#     if i > m:
#         m = i
# print(m)

# ====================
# Ques2 Write a Python program that takes a list of integers and prints the sum of all numbers greater than 10.

# a = list(map(int, input().split()))
# s = 0
# for i in a:
#     if i > 10:
#         s+=i
# print(s)

# ===================================
# Ques3: Write a Python program that takes a list of integers and finds the second largest unique number without using sort() or max().

# a = list(map(int, input().split()))

# newArr = []
# for num in a:
#     if a.count(num) == 1:
#         newArr += [num]  
# if len(newArr) < 2:
#     print("There is no second largest unique number.")
# else:
#     m1 = 0  
#     m2 = newArr[0] 
    
#     for i in newArr:
#         if i > m1:
#             m2 = m1  
#             m1 = i  
#         elif i > m2:
#             m2 = i   
            
#     print(m2)

# =================================
# https://leetcode.com/problems/squares-of-a-sorted-array/description/?clckid=70ab4e0c&utm_source=chatgpt.com
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         l = 0
#         r = len(nums) -1 
#         result = [0]*len(nums)
#         p = len(nums) -1
#         while l<=r:
#             if abs(nums[l])> abs(nums[r]):
#                 result[p] = nums[l]**2
#                 l+=1
#             else:
#                 result[p] = nums[r]**2
#                 r-=1
#             p-=1
#         return result 