# Q1 Login Attempt Monitor 🔐
# A system logs login attempts as a list of "Success" / "Fail" strings for one user. If a user has 3 consecutive failed attempts, the account should be locked immediately at that point, print the index where it got locked. If it never happens, print "Account Safe".

# Input: ["Success", "Fail", "Fail", "Success", "Fail", "Fail", "Fail"]
# Output: Account locked at index 6

# Constraint: You cannot use .count(). Use loop.
# a = list(map(str, input().split()))
# c = 0
# for i in range(len(a)):
#     if a[i].lower() == "fail":
#         c+=1
#     else:
#         c =0
#     if c >= 3:
#         print("Locked at index", i)
#         break
# else:
#     print("Safe")

# ===========================================
# Q2 Server Response Time Alert 🖥️ 
# A server logs its response time (in ms) every second. Find the longest streak of consecutive readings that stayed below 200ms (considered "healthy"). Print the length of that streak.
# Input: [180, 190, 250, 150, 170, 190, 300, 100, 120]
# Output: Longest healthy streak = 3
# eg: (150, 170, 190 → 3 in a row under 200)

# a = list(map(int, input().split()))
# c = 0
# m = 0
# for i in a:
#     if i < 200:
#         c+=1
#     else:
#         c = 0
#     if c > m:
#         m = c
# print(m)

# ========================
 
# Q3 Weekly Attendance Grid 🗓️

# An office tracks attendance for 3 employees over 5 days using a 2D list, where 1 = present, 0 = absent. Find which employee has the most absences, and print their name with total absent days. 

# Input: [[1,1,0,1,1], [0,0,1,1,1], [1,1,1,1,1]]
# Output: Employee B has the most absences: 2

# a = [list(map(int, input().split())) for _ in range(3) ]

# m = 0
# e = ""

# for i in a:
#     c = 0
#     for j in range(len(i)):
#         if i[j] == 0:
#             c+=1
#         if c > m:
#             m = c
#             if j == 0:
#                 e = "A"
#             elif j == 1:
#                 e = "B"
#             else:
#                 e = "C"
# print(f"Employe {e} has the most absence {m}")

# =================
# https://leetcode.com/problems/valid-palindrome/description/?utm_source=chatgpt.com

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = "".join(c for c in s if c.isalnum()).lower()

#         l = 0
#         r = len(s) -1
#         while l <=r:
#             if s[l]!=s[r]:
#                 return False
#             l+=1
#             r-=1
#         return True


# ==================================
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/?envId=top-interview-150&envType=study-plan-v2&utm_source=chatgpt.com

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         l = 0
#         r = len(numbers)-1
#         while l <=r:
#             s = numbers[l]+numbers[r]
#             if s == target:
#                 return [l+1,r+1]
#             elif s > target:
#                 r -=1
#             else:
#                 l+=1
        
# ==========================
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?lang=c&utm_source=chatgpt.com

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         s = 0
#         for f in range(1, len(nums)):
#             if nums[s] != nums[f]:
#                 s+=1
#                 nums[s] = nums[f]
#         return s+1

# =============================

# Ques2 Write a program to find the second largest number in a list without using sort(), sorted(), or max(). Use a loop and conditionals only.

# Input: [10, 5, 20, 8, 20, 15]
# Output: 15


# a = list(map(int, input().split()))
# m = 0
# m2 = 0
# for i in range(len(a)):
#     if a[i] > m:
#         m = a[i]
#     if a[i] > m2 and a[i] != m:
#         m2 = a[i]
# print(m2)

