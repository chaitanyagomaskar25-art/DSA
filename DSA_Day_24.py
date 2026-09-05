# Given an array containing positive and negative integers, find the length of the longest contiguous subarray whose sum is exactly K.
# Input
# 8
# 3 4 -7 1 3 3 1 -4
# 7
# Output
# 6
# n = int(input())
# a = list(map(int, input().split()))
# k = int(input())
# s = 0
# m = 0
# l = 0
# for i in range(n):
#     s+=a[i]
#     c+=1
#     while s >=k:
#         m = max(m, i-l+1)
#         s -= a[l]
#         l+=1
# print(m)


# =======================================
# Given an array where each element represents the height of a bar, calculate how much rainwater can be trapped after raining.

# Input

# 6
# 4 2 0 3 2 5

# Output

# 9

# ===================================
# Q1: Sum of Even Numbers ➕
# Given a list of numbers, add up only the even ones.

# Input: [1,2,3,4,5,6,7,8]
# Output: 20

# a = list(map(int, input().split()))
# s = 0
# for i in a:
#     if i%2==0:
#         s+=i
# print(s)

# ============================
# Q2: FizzBuzz Range 🎯
# Print numbers from start to end. Replace multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz". 

# Input: start=1, end=15
# Output: ['1','2','Fizz','4','Buzz','Fizz','7','8','Fizz','Buzz','11','Fizz','13','14','FizzBuzz']

# s = int(input())
# e = int(input())
# result = []
# while s <=e:
#     if s%3 ==0 and s%5 == 0:
#         result.append("fizzBuzz")
#     elif s% 3 == 0:
#         result.append("fizz")
#     elif s%5==0:
#         result.append("Buzz")
#     else:
#         result.append(s)
#     s+=1
# print(result)

# ======================================
# Q3: Armstrong Number Checker 🔢
# Check if a number is an "Armstrong number" — each digit raised to the power of the total digit count, summed up, equals the original number. 

# Input: 153
# Output: True   (1³ + 5³ + 3³ = 1+125+27 = 153)

# n = int(input())
# s = 0
# m = n
# while n >0:
#     d = n%10
#     s += d**3
#     n //= 10
# if s == m:
#     print("Yes")
# else:
#     print("NO")

# =====================================
# Q4: Segregate Negatives and Positives (Stable) ➖➕
# Rearrange an array so all negative numbers come first, followed by all positive numbers — keeping their original relative order within each group. 

# Input: [1, -2, 3, -4, 5, -6, 7]
# Output: [-2, -4, -6, 1, 3, 5, 7]

# a = list(map(int, input().split()))
# l = 0
# for f in range(len(a)):
#     if a[f] <0:
#         a[l], a[f] = a[f], a[l]
#         l+=1
# print(a)

# =========================================

# Q1: Count Uppercase Letters 🔠
# Count how many uppercase letters appear in a sentence. 

# Input: "Hello World From India"
# Output: 4

# s = input()
# c = 0
# for i in s:
#     if i.isupper():
#         c+=1
# print(c)

# =====================================
# Q2: Count Words Starting with a Vowel 🔤
# Count how many words in a sentence start with a vowel. 

# Input: "Akriti is eating an apple today"
# Output: 5

# s = input()
# a = s.split(" ")
# c = 0
# for i in a:
#     if i[0].lower() in "aieou":
#         c+=1
# print(c)

# ==============================

# Q3: String Rotation Checker 🔄
# Check if one string is a rotation of another (e.g., "bottlewater" is "waterbottle" rotated).

# Input: "waterbottle", "bottlewater"
# Output: True

# s1 = "".join(sorted(input()))
# s2 = "".join(sorted(input()))
# if s1.lower() in s2.lower() or s2.lower() in s1.lower():
#     print("Yes")
# else:
#     print("No")

# =========================================
# Q4: Diamond Star Pattern : 
# Print a diamond shape made of stars, given the number of rows for the top half.

# Input: n=4

n = int(input())
str = ""
for i in range(n):
    str+="* "
    print(str)

str = ""
i = 1
while i <0:
    for i in range(n-i):
        str+=" "
    str+="*"
    i+=1
    print(str)