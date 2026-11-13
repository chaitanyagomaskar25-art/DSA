# Mask all except last 4 digits of credit card string:
# Input: "1234567812345678" | Output: "************5678"


# s = input()
# if len(s) == 16:
#     print("*"*12 + s[-4:])
# else:
#     print("Invalid credit card")



# =====================================

# Convert snake_case to camelCase:
# Input: "user_first_name" | Output: "userFirstName"

# s = input()

# a = s.split("_")
# newS = a[0]
# for i in range(1, len(a)):
#     newS+= a[i].capitalize()

# print(newS)

# =====================================

# Convert camelCase to snake_case:
# Input: "userFirstName" | Output: "user_first_name"

# s = input()

# newS = ""
# for i in range(0, len(s)):
#     if s[i].isupper():
#         newS+= "_" + s[i].lower()
#     else:
#         newS+=s[i]
    
# print(newS)

# =====================================

# Convert string to kebab-case:
# Input: "Hello World Page" | Output: "hello-world-page"

# s = input()

# a = s.split(" ")
# newS = ""
# for i in range(0, len(a)):
#     if i != len(a)-1:
#         newS+= a[i].lower() + "-"
#     else:
#         newS+=a[i].lower()

# print(newS)


# =====================================
# Check if string starts with given prefix:
# Input: str = "unbelievable", prefix = "un" | Output: true

# s = input()
# p = input()
# print(s.startswith(p))

# =====================================

# Check if string ends with given suffix:
# Input: str = "document.pdf", suffix = ".pdf" | Output: true



# s = input()
# p = input()
# print(s.endswith(p))


# =====================================

# Insert character every K characters:
# Input: str = "12345678", ch = '-', K = 2 | Output: "12-34-56-78"

# s = input()
# ch = input()
# k = int(input())

# newS = ch.join(s[i : i + k] for i in range(0, len(s), k)) 
# print(newS)

# =====================================
