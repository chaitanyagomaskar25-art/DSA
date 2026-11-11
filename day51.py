# Length of a string: Count characters without using built-in length method.
# Input: "hello world" | Output: 11

# s = input()
# print(len(s))

# ============================
# Reverse a string: Reverse characters in place or using a loop.
# Input: "javascript" | Output: "tpircsavaj"

# s = input()
# print(s[::-1])

# ============================

# Check palindrome: Determine if string reads same backward.
# Input: "racecar" | Output: true

# s = input()
# l = 0
# r = len(s)-1
# while l<=r:
#     if s[l]!=s[r]:
#         print(False)
#         break
#     l+=1
#     r-=1
# else:
#     print(True)

# ============================

# Count vowels and consonants: Count occurrences of each in alphabetic string.
# Input: "programming" | Output: Vowels: 3, Consonants: 8

# s = input()

# v = 0
# c = 0
# for i in s:
#     if i in "aeiou":
#         v+=1
#     else:
#         c+=1

# print(v,c)


# ============================


# Count uppercase, lowercase, digits, and special characters:
# Input: "Pass123!#" | Output: Upper: 1, Lower: 3, Digits: 3, Special: 2

# a = input()

# u = 0
# l = 0
# d = 0
# s = 0

# for i in a:
#     if i.isdigit():
#         d+=1
#     elif i.isupper():
#         u+=1
#     elif i.islower():
#         l+=1
#     else:
#         s+=1

# print(u,l,d,s)



# ============================

# Convert lowercase to uppercase: Without using standard uppercase built-in.
# Input: "coder" | Output: "CODER"


# s = input()
# print(s.upper())


# ============================

# Convert uppercase to lowercase: Without using standard lowercase built-in.
# Input: "GITHUB" | Output: "github"


# s = input()
# print(s.lower())

# ============================

# Toggle character case: Invert casing of each letter.
# Input: "NavGurukul" | Output: "nAVgURUKUL"


# s = input()
# result = ""


# for i in s:
#     if i.islower():
#         result += i.upper()
#     else:
#         result += i.lower()

# print(result)

# ============================

# Remove spaces: Strip all whitespace characters from text.
# Input: "a b c d" | Output: "abcd"


# s = input()
# a = s.split(" ")

# print("".join(a))

# ============================

# Count words in a sentence: Count sequences separated by spaces.
# Input: "Practice makes a person perfect" | Output: 5

# s = input()
# a = s.split(" ")
# print(len(a))


# ============================


# Find character frequency: Return frequency count of every character.
# Input: "apple" | Output: {a: 1, p: 2, l: 1, e: 1}


# s = input()
# f = {}
# for i in s:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1

# print(f)

# ============================

# Find first non-repeating character: Return first unique character.
# Input: "swiss" | Output: "w"

# s = input()
# f = {}
# for i in s:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1

# for i in f:
#     if f[i] == 1:
#         print(i)
#         break
# else:
#     print(-1)

# ============================

# Find first repeating character: Return first character that repeats.
# Input: "geeks" | Output: "e"


# s = input()
# f = {}
# for i in s:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1

# for i in f:
#     if f[i] != 1:
#         print(i)
#         break
# else:
#     print(-1)

# ============================

# Find maximum occurring character: Return character with highest frequency.
# Input: "success" | Output: "s"


# s = input()
# f = {}
# for i in s:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1

# m = 0
# k = ""
# for i in f:
#     if f[i] > m:
#         m = f[i]
#         k = i
# print(k)



    
# ============================


# Remove all vowels from string:
# Input: "beautiful" | Output: "btfl"


# s = input()
# for i in s:
#     if i in "aeiou":
#         s = s.replace(i, "")

# print(s)


# ============================

# Remove duplicate characters: Keep only first occurrence of each character.
# Input: "banana" | Output: "ban"



# s = input()
# f = {}
# for i in s:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1

# newS = ""
# for i in f:
#     newS+=i

# print(newS)


# ============================


# Check if two strings are of equal length:
# Input: "abc", "def" | Output: true


# a = input()
# b = input()

# print(True) if len(a) == len(b) else print(False)


# ============================

# Concatenate two strings manually:
# Input: "hello", "world" | Output: "helloworld"


# a = input()
# b = input()

# print(a+b)

# ============

# Compare two strings lexicographically: Return -1, 0, or 1.
# Input: "apple", "banana" | Output: -1

# a = input()
# b = input()

# if a< b:
#     print(-1)
# elif a == b:
#     print(0)
# else:
#     print(1)

# ============================


# Copy one string to another manually:
# Input: "source" | Output: "source"

# a = input()
# b = ""
# for i in a:
#     b+=i

# print(b)





