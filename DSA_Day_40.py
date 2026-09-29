# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# num1 = list(map(int, input().split()))
# num2 = list(map(int, input().split()))

# for i in range(len(num2)):
#     j = 0
#     while j < len(num1) and num2[i] > num1[j]:
#         j+=1      
#     num1.insert(j, num2[i])

# if len(num1) % 2 == 0:
#     mid = (num1[len(num1)//2] + num1[(len(num1)//2) -1]) / 2
# else:
#     mid = num1[len(num1)//2]

# print(mid)



# ============================================

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3

# Example 2:

# Input: s = "LVIII"
# Output: 58

# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994

# s = input("Enter a roman digit: ").upper()
# roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# total = 0
# n = len(s)
# for i in range(n):
#     if i < n - 1 and roman[s[i]] < roman[s[i + 1]]:
#         total -= roman[s[i]]
#     else:
#         total += roman[s[i]]

# print(total)



# =====================================================

