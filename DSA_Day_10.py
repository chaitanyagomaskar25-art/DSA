# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/POOK?tab=statement
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     if n == 3 or n== 2:
#         print(n-1)
#     else:
#         print(n)
     
    
# ============================

# Ques1
# Write a Python program that takes a number as input and prints its square.
# Input: 7
# Output: 49

# n = int(input())
# print(n*n)


# ===========================
# Ques2
# Write a Python program that takes a number as input and calculates and prints its square root.
# Input: 81
# Output: 9

# n = int(input())
# print(int(n**0.5))

# ========================

# Ques3
# Write a Python program that takes a list of integers and prints the sum of squares of all even numbers in the list.
# Input: [1, 2, 3, 4, 5, 6]
# Output: 56   (2² + 4² + 6² = 4+16+36)

# a = list(map(int, input().split()))
# sum = 0
# for i in a:
#     if i % 2 == 0:
#         square = i*i
#         sum+= square
# print(sum)

# =====================

# Ques4
# Write a Python program that takes a list of positive integers and prints the square root of the largest perfect square present in the list. Ignore numbers that are not perfect squares.
# Input:
# [16, 25, 10, 49, 30, 81, 17]
# Output:
# 9

# a = list(map(int, input().split()))
# def is_perfect_square(n):
#     if n< 0:
#         return False
#     if n < 2:
#         return True
#     low = 2
#     high = n//2
#     while low<=high:
#         mid = (low+high) //2
#         square = mid*mid
#         if square == n:
#             return True
#         elif square < n:
#             low = mid+1
#         else:
#             high = mid-1
#     return False
# perfect = [i for i in a if is_perfect_square(i)]

# if perfect:
#     print(max(perfect))
# else:
#     print("No perfect square found")

# ======================


# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/?utm_source=chatgpt.com

# class Solution:
#     def minStartValue(self, nums: List[int]) -> int:
#         prefix = []
#         total = 0
#         for i in nums:
#             total += i
#             prefix.append(total)
        
#         minVal = min(prefix)
#         if minVal < 0:
#             return abs(minVal)+1
#         else:
#             return 1


# ================================
# https://leetcode.com/problems/count-vowel-strings-in-ranges/?utm_source=chatgpt.com

# class Solution:
#     def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
#         a = []
#         vowel = "aeiou"
#         for i in words:
#             if i[0] in vowel and i[-1] in vowel:
#                 a.append(1)
#             else:
#                 a.append(0)
#         prefix = [0]
#         for i in a:
#             prefix.append(prefix[-1] + i)
#         ans = []
#         for i in queries:
#             l = i[0]
#             r = i[-1]
#             ans.append(prefix[r+1] - prefix[l])
#         return ans
# *****************optimized way for this ********************
# vowel = {"a", "e", "i", "o", "u"}
# prefix = [0]
# for w in words:
#     is_vowel = 1 if (w[0] in vowel and w[-1] in vowel) else 0
#     prefix.append(prefix[-1]+is_vowel)
#     return [prefix[r+1]-prefix[l] for l, r in queries]


# ============================

