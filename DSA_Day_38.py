# Q1 — Word Score Calculator

# You are given a word:

# word = "python"

# Calculate its score using these rules:

# 1. Every vowel (a, e, i, o, u) = 2 points
# 2. Every consonant = 1 point
# 3. Print each character and its points.
# 4. Print the total score of the word.

# Expected output:

# p -> 1
# y -> 1
# t -> 1
# h -> 1
# o -> 2
# n -> 1

# Total Score: 7


# words = input("Enter a word: ")
# t = 0

# for i in words:
#     if i.lower() in "aeiou":
#         t+=2
#         print(f"{i}->2")
#     else:
#         t+=1
#         print(f"{i}-> 1")
    
# print(f"Total Score: {t}")



# ======================================

# Q2 — Temperature Change Detector

# A weather station records temperatures for 7 days:

# temperatures = [28, 31, 29, 29, 33, 30, 35]

# For every day after the first day:

# Compare the temperature with the previous day.
# Print:
# 1. "Increased by X" if it went up.
# 2. "Decreased by X" if it went down.
# 3. "No Change" if it stayed the same.

# Expected output:

# Day 2: Increased by 3
# Day 3: Decreased by 2
# Day 4: No Change
# Day 5: Increased by 4
# Day 6: Decreased by 3
# Day 7: Increased by 5

# temp = list(map(int, input("Enter a temprature: ").split()))

# for i in range(1, len(temp)):
#     if temp[i] > temp[i-1]:
#         print(f"Day {i+1} : Increase by {temp[i] - temp[i-1]}")
#     elif temp[i] < temp[i-1]:
#         print(f"Day {i+1} : Decreased by {temp[i-1] - temp[i]}")
#     else:
#         print(f"Day {i+1} : No changes")
        

# =========================================
# Q3 — Alternating Array Builder

# You have two arrays:

# boys = ["Amit", "Rahul", "Kiran", "Arjun"]
# girls = ["Priya", "Neha", "Sneha", "Pooja"]

# Create a new list by taking elements alternately from the two arrays:

# Amit, Priya, Rahul, Neha, Kiran, Sneha, Arjun, Pooja

# Rules:

# 1. Take one name from boys.
# 2. Then one name from girls.
# 3. Continue until both lists are finished.
# 4. Store the result in a new list.
# 5. Print the final list.
# 6. Also print the total number of names.

# Expected output:

# [Amit, Priya, Rahul, Neha, Kiran, Sneha, Arjun, Pooja]

# Total Names: 8

# b = list(map(str, input("Enter boys names : ").split()))
# g = list(map(str, input("Enter girls names : ").split()))

# f = []

# i = 0
# while i < len(b) and i < len(g):
#     f.append(b[i])
#     f.append(g[i])
#     i+=1

# f.extend(b[i:])

# print(f, f"\nTotal Names: {len(f)}")
