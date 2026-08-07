# Alternating String (1116)

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s = "".join(sorted(input()))
#     c1 = s.count("1")
#     c0 = s.count("0")
#     if c1 == c0:
#         print(c1+c0)
#     elif c1 > c0:
#         print((c0*2)+1)
#     else:
#         print((c1*2)+1)

# ===================

# Problem 1: Decode the Message
# Each number represents an ASCII code.
# Convert all numbers into characters and print the hidden message.
# Input: 72 69 76 76 79
# Output: HELLO

# a = list(map(int, input().split()))
# s = ""
# for i in a:
#     s+= str(chr(i))
# print(s)
# ==============
# Problem 2: Hide the Vowels
# Replace every vowel (A, E, I, O, U) with *.
# Input: HELLO
# Output: H*LL*

# s = input()
# for i in s:
#     if i == "a" or i == "e" or i =="i" or i =="o" or i =="u":
#         s = s.replace(i, "*")
# print(s)
# =====================

# Problem 3: Longest Word
# Words are separated by a space character (ASCII 32).
# Find the longest word in the decoded message.
# Input: HELLO WORLD CHATGPT
# Output: CHATGPT

# s = input()
# a = s.split(" ")

# maxl = 0
# maxs = ""
# for i in a:
#     if len(i) > maxl:
#         maxl = len(i)
#         maxs = i
# print(maxs)

# =======================
# Problem 4: Frequency Analysis
# Find the most frequently occurring alphabet in the decoded message.
# Ignore spaces.
# If two letters have the same frequency, print the alphabet that appears first

# message = input()
# frequency = {}
# order = []

# for char in message:
#     if char == " ":
#         continue
#     if char not in frequency:
#         frequency[char] = 0
#         order.append(char) 
#     frequency[char] += 1

# max_char = ""
# max_freq = 0
# for char in order:
#     if frequency[char] > max_freq:
#         max_freq = frequency[char]
#         max_char = char

# print(max_char)

# =====================
# Problem 1: Find the First Empty Parking Slot
# A parking lot has N parking slots.
# Each slot contains:
# 0 → Empty
# 1 → Occupied
# Find the index of the first empty parking slot.
# If all slots are occupied, print "Parking Full".
# Input: 1 1 1 0 1 0
# Output: 3

# a = list(map(int, input().split()))
# for i in range(len(a)):
#     if a[i] == 0:
#         print(i)
#         break
# else:
#     print("Parking Full")


# ==============================
# Problem 2: Largest Continuous Empty Area
# Find the longest continuous sequence of empty parking slots.
# Input: 1 0 0 0 1 0 0
# Output: Length = 3

# a = list(map(int, input().split()))
# n = len(a)
# c = 0
# maxl = 0
# for i in range(n):
#     c = 0
#     if a[i] == 0:
#         c+=1
#         for j in range(i+1, n):
#             if a[j] == 0:
#                 c +=1
#             else:
#                 break
#         if c > maxl:
#             maxl = c
# print(maxl)
        
        
# =========================
# Problem 3: Bus Parking
# A bus requires K consecutive empty slots.
# Determine whether the bus can be parked.
# Input: Slots:1 0 0 0 1 0 0
#            K = 3
# Output: YES

# a = list(map(int, input().split()))
# k = int(input())
# n = len(a)
# c = 0
# maxl = 0
# for i in range(n):
#     c = 0
#     if a[i] == 0:
#         c+=1
#         for j in range(i+1, n):
#             if a[j] == 0:
#                 c +=1
#             else:
#                 break
#     if c == k:
#         print("yes")
#         break
# else:
#     print("no")


# ============================
# Problem 4: Best Parking Location
# If there are multiple locations where the bus can park, choose the parking block that lies in the middle among all the valid parking locations.
# If the number of valid parking locations is odd, choose the exact middle one.
# If the number of valid parking locations is even, choose the left-middle parking location.
# Print the starting index of the selected parking block.
# Input: Parking Slots: 0 0 0 1 0 0 0 1 0 0 0
# Output: 5

