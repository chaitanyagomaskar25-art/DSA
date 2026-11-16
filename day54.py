# Sort characters of a string alphabetically:
# Input: "edcba" | Output: "abcde"


# a = input()
# print(''.join(sorted(a)))


# =============================================

# Sort characters by descending frequency:
# Input: "tree" | Output: "eert" (or "eetr")

# a = input()
# print("".join(sorted(a)))


# =============================================

# Check if string contains binary representation only:
# Input: "1011001" | Output: true; Input: "10201" -> false


# s = input()
# s = s.replace("1", "")
# s = s.replace("0", "")

# print(True) if len(s) == 0 else print(False)

# =============================================

# Validate standard IPv4 address format:
# Input: "192.168.1.1" | Output: true; Input: "256.100.0.1" -> false

# s = input()
# a = [int(x) for x in s.split(".")]

# for i in a:
#     if i > 255 or i < 0:
#         print(False)
#         break
# else:
#     print(True)

# =============================================

# Generate acronym from string:
# Input: "As Soon As Possible" | Output: "ASAP"

# s = input()

# a =  s.split(" ")
# result = ""

# for i in a:
#     result += i[0].upper()

# print(result)


# =============================================

# Find length of the last word in string:
# Input: "fly me to the moon " | Output: 4


# s = input()
# a = s.strip().split(" ")
# print(len(a[-1]))


# =============================================
# Repeat each character K times:
# Input: str = "abc", K = 2 | Output: "aabbcc"


# s = input()
# k = int(input())

# result = ""
# for i in s:
#     result += (i * k)

# print(result)

# =============================================

# Pad string to target length with symbol (Left Pad):
# Input: str = "42", target = 5, pad = '0' | Output: "00042"

# s = input()
# t = int(input())
# totalLength = t - len(s)
# p = input()

# print((p*totalLength)+s)


# =============================================

# Pad string to target length with symbol (Right Pad):
# Input: str = "hi", target = 5, pad = '*' | Output: "hi***"

# s = input()
# t = int(input())
# totalLength = t - len(s)
# p = input()

# print(s+ (p*totalLength))


# =============================================

# Truncate text with ellipsis if length exceeds limit:
# Input: str = "Frontend Mentor", max = 8 | Output: "Front..."

# text = input()
# max_len = int(input())

# if len(text) <= max_len:
#     print(text)
# elif max_len < 3:
#     print("." * max_len)
# else:
#     print(text[:max_len - 3] + "...")

# =============================================

# Determine if one string is a rotation of another:
# Input: s1 = "waterbottle", s2 = "erbottlewat" | Output: true

# a = input()
# b = input()
# if "".join(sorted(a.strip())) == "".join(sorted(b.strip())):
#     print(True)
# else:
#     print(False)



# =============================================