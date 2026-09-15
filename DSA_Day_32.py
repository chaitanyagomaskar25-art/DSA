# Q3: Chessboard Pattern Printer ♟️ (Nested Loop) 
# Print an N x N chessboard pattern using # for one color square and . for the other, alternating so it looks like a real chessboard.
# INPUT: 5
# OUTPUT:              #.#.#
#                               .#.#.
#                              #.#.#
#                               .#.#.
#                              #.#.#

# n = int(input())

# for i in range(n*2-1):
#     str = ""
#     if i % 2 == 0:
#         for j in range(n*2-1):
#             if j % 2 ==0:
#                 str+="#"
#             else:
#                 str+="."
#     else:
#         for j in range(n*2-1):
#             if j % 2 ==0:
#                 str+="."
#             else:
#                 str+="#"
#     print(str)

# for i in range(n*2-1):
#     str = ""
#     if i %2==0:
#         str+="#"
#     else:
#         str+="."
#     for i in range(n*2-2):
#         if str[len(str)-1] == "#":
#             str+="."
#         else:
#             str+="#"
#     print(str)

# ===================================================


# Q2: Vowel Counter per Word 🔤
# Given a sentence, split it into words manually and count the number of vowels in each word.

# INPUT: "the quick brown fox"
# OUTPUT: [('the', 1), ('quick', 2), ('brown', 1), ('fox', 1)]

# a = input()
# s = a.split()
# result = []
# for i in s:
#     c = 0
#     for j in i:
#         if j.lower() in "aieou":
#             c+=1
#     result.append((i, c))
# print(result)

# ==============================================
# Q1: Longest Palindromic Substring 🔍
# Find the longest substring within a string that reads the same forwards and backwards.

# Input: "babad"
# Output: "bab"   (or "aba" — either is valid)


# a = input()
# result = []
# n = len(a)
# for i in range(n):
#     for j in range(n):
#         s = a[i:n-j+1]
#         if s not in result:
#             result.append(s)
# m = 0
# ms = ""
# for i in result:
#     l = 0
#     r = len(i)-1
#     while l <= r:
#         if i[l]!=i[r]:
#             break
#         l+=1
#         r-=1
#     else:
#         if len(i)-1 > m:
#             m = len(i)-1
#             ms = i
# print((m, ms))

