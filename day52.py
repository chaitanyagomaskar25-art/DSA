# Count total punctuation marks:
# Input: "Hello, world! How are you?" | Output: 3


# s = input()
# c = sum(s.count(char) for char in "./!?,")
# print(c)


# ===============================

# Replace all occurrences of a character: Replace old char with new char.
# Input: s = "banana", old = 'a', new = 'o' | Output: "bonono"


# s = input()
# old = input()
# new = input()

# s = s.replace(old, new)
# print(s)


# ===============================

# Remove a specific character:
# Input: s = "elephant", ch = 'e' | Output: "lphant"

# s = input()
# old = input()

# s = s.replace(old, "")
# print(s)

# ===============================

# Check if string contains only digits:
# Input: "12345" | Output: true; Input: "12a45" -> false

# s = input()
# for i in s:
#     if not i.isdigit():
#         print(False)
#         break
# else:
#     print(True)


# ===============================

# Check if string contains only alphabets:
# Input: "Welcome" | Output: true; Input: "Welcome1" -> false

# s = input()
# for i in s:
#     if not i.isalpha():
#         print(False)
#         break
# else:
#     print(True)


# ===============================

# Find index of first occurrence of character:
# Input: s = "developer", ch = 'v' | Output: 2

# s = input()
# char = input()


# for i in range(len(s)):
#     if s[i] == char:
#         print(i)
#         break
# else:
#     print(-1)

# ===============================

# Find index of last occurrence of character:
# Input: s = "developer", ch = 'e' | Output: 7


# s = input()
# char = input()


# for i in range(len(s)-1, -1, -1):
#     if s[i] == char:
#         print(i)
#         break
# else:
#     print(-1)


# ===============================

# Print all individual characters on a new line:
# Input: "cat" | Output: 'c', 'a', 't'


# s = input()
# for i in s:
#     print(i)


# ===============================

# Reverse words in a sentence: Maintain character order within words.
# Input: "I love coding" | Output: "coding love I"

# s = input()
# a = s.split(" ")
# newS = " ".join(a[::-1])
# print(newS)

# ===============================

# Reverse each individual word: Keep word positions intact.
# Input: "I love coding" | Output: "I evol gnidoc"


# s = input()
# a = s.split(" ")

# newS = ""
# for i in a:
#     newS += " " + i[::-1]

# print(newS.strip())


# ===============================

# Capitalize first letter of every word (Title Case):
# Input: "full stack web development" | Output: "Full Stack Web Development"


# s = input()
# a = s.split(" ")
# for i in range(len(a)):
#     a[i] = a[i].capitalize()

# print(" ".join(a))

# ===============================

# Check Valid Anagram: Determine if two strings have identical character frequencies.
# Input: "listen", "silent" | Output: true


# a = input()
# b = input()

# if sorted(a) == sorted(b):
#     print("yes")
# else:
#     print("No")



# ===============================

# Check Pangram: Determine if string contains every letter of English alphabet.
# Input: "The quick brown fox jumps over the lazy dog" | Output: true

# s = input()
# s_lower = s.lower()
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# is_pangram = True
# for char in alphabet:
#     if char not in s_lower:
#         is_pangram = False
#         break

# print(is_pangram)

# ===============================

# Check Isomorphic Strings: Letters in first map one-to-one to second.
# Input: "egg", "add" | Output: true; Input: "foo", "bar" -> false





# ===============================


# Valid Palindrome after stripping non-alphanumeric: Case-insensitive.
# Input: "A man, a plan, a canal: Panama" | Output: true


# s = input()
# a = "".join(i.lower() for i in s if i.isalpha())

# l = 0
# r = len(a)-1
# while l<=r:
#     if a[l] != a[r]:
#         print(False)
#         break
#     l+=1
#     r-=1

# else:
#     print(True)

# ===============================

# Valid Palindrome II (at most one deletion permitted):
# Input: "abca" | Output: true (remove 'b' or 'c')


# s = input()

# def is_palindrome(st):
#     l = 0
#     r = len(st) - 1

#     while l < r:
#         if st[l] != st[r]:
#             return False
#         l += 1
#         r -= 1

#     return True


# if is_palindrome(s):
#     print(True)
# else:
#     for i in range(len(s)):
#         newS = s[:i] + s[i+1:]
#         print(newS)
#         if is_palindrome(newS):
#             print(True)
#             break
#     else:
#         print(False)


# ===============================

# Count number of vowels at odd indices: (0-indexed).
# Input: "elephant" | Output: 1 (index 1: 'l', 3: 'p', 5: 'a' -> 1)

# s = input()
# f = {}
# c = 0
# for i in range(1, len(s), 2):
#     if s[i] in "aeiou":
#         c+=1
#     f[i] = s[i]

# print(f , c)

# ===============================

# # Swap first and last characters of each word:
# # Input: "hello world" | Output: "oellh dorlw"

# s = input()
# a = s.split(" ")
# for i in range(len(a)):
#     a[i] = a[i][-1] + a[i][1:-1] + a[i][0]

# print(" ".join(a))


# ===============================

# # Trim leading and trailing whitespace manually:
# # Input: " clean code " | Output: "clean code"

# s = input()
# print(s.strip())

# ===============================

# # Compress consecutive multiple spaces into a single space:
# # Input: "react node express" | Output: "react node express"

# s = input()
# print(" ".join(s.split()))


# ===============================


