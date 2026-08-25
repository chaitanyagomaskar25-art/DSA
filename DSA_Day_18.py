# 1. Count File Types
# Problem
# A file upload service receives different types of files.
# Count how many files belong to each extension.
# Input
# [
# "resume.pdf",
# "photo.jpg",
# "notes.pdf",
# "logo.png",
# "image.jpg"
# ]
# Expected Output
# {
# pdf:2,
# jpg:2,
# png:1
# }


# a = list(map(str, input().split()))
# b = [i.split(".")[1] for i in a]
# newObj = {}
# for i in b:
#     if i in newObj:
#         newObj[i] +=1
#     else:
#         newObj[i] = 1
# print(newObj)

# =======================================
#  Reverse Username
# Input:
# Rinki
# Output:
# ikniR

# name = input()
# reversedName = ""
# for i in range(len(name)-1, -1, -1):
#     reversedName += name[i]
# print(reversedName)

# ==============================
 	
# 3. Capitalize First Letter
# Input
# javascript
# Output
# Javascript
# s = input()
# s = s[0].upper() + s[1:]
# print(s)


# =======================
# Q1: Vowel Counter per Word 🔤
# Given a sentence, split it into words manually and count the number of vowels in each word.

# INPUT: "the quick brown fox"
# OUTPUT: [('the', 1), ('quick', 2), ('brown', 1), ('fox', 1)]

# a = input()
# b = a.split(" ")
# result = []
# for i in b:
#     c = 0
#     for j in i:
#         if j in "aieou":
#             c+=1
#     result.append((i, c))
# print(result)

# ============================
# Q2: Truck Overload Checker 🚛
# A logistics company loads pallets onto trucks. Each truck has a weight limit of 100 kg. Given a 2D list where each row is a truck's pallet weights, find all overloaded trucks and by how much.

# INPUT: [[20, 35, 15], 
#              [40, 35, 30], 
#              [45, 40, 30]]

# OUTPUT: Overloaded trucks (truck_no, excess_weight): [(2, 5), (3, 15)]

# n = int(input())
# a = [list(map(int, input().split())) for i in range(n)]
# result = []
# for i in range(n):
#     c = sum(a[i])
#     if c > 100:
#         rem = c-100
#         result.append((i+1, rem))
# print(result)

# ====================================
# Q3: Username Generator 👤
# A system needs to auto-generate a username from a person's full name, following these rules:
# Remove all spaces
# Keep only letters (ignore any numbers or symbols if present)
# Convert everything to lowercase
# Keep only the first 8 characters

# INPUT: "Priyanka Chopra Jonas"
# OUTPUT: priyanka

# a = input()
# a = "".join([i for i in a if i.isalpha()]).lower()
# print(a[:8])


# ========================

# Q4: Anagram Group Finder (No Dictionary)
# Group a list of words into sets of anagrams — words that contain the exact same letters, just rearranged.

# INPUT: ["eat", "tea", "tan", "ate", "nat", "bat"]
# OUTPUT: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
