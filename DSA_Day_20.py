# Q1: Vowel-Consonant Balancer ⚖️
# Given a word, print whether it has more vowels, more consonants, or an equal count.

# Input: "programming"
# Output: More Consonants (3 vowels, 8 consonants)

# s = input()
# v = 0
# c = 0
# for i in s:
#     if i.lower() in "aieou":
#         v+=1
#     else:
#         c+=1
# if v >c:
#     print("More Vowels")
# elif v <c:
#     print("More Consonant")
# else:
#     print("Both are equal")


# ======================================
# Q2: Digit Sum Reducer 🔢
# Given a number, keep adding its digits together until only a single digit remains.

# Input: 9875
# Output: 2
# Example:  (9+8+7+5=29 → 2+9=11 → 1+1=2)

# n = int(input())
# while n >= 10:
#     s = 0
#     while n >0:
#         s+= n%10
#         n = n //10
#     n = s
# print(s)

# ==========================================
# Q3: Zigzag Array Checker 〰️
# Check if an array is "zigzag" - every element is alternately greater than or smaller than its neighbors. 

# Input: [1, 5, 2, 8, 3]
# Output: True

# a = list(map(int, input().split()))
# if len(a) < 2:
#     print(True)
# else:
#     isgreater = a[1]>a[0]
#     if a[1] == a[0]:
#         print(False)
#     else:
#         for i in range(1, len(a)-1):
#             isgreater = not isgreater
#             if isgreater and (a[i+1]<= a[i]):
#                 print(False)
#                 break
#             if not isgreater and (a[i+1] >= a[i]):
#                 print(False)
#                 break
#         else:
#             print(True) 

# ===============================
# Q4: Tic-Tac-Toe Winner Checker
# Given a 3x3 board ("X", "O", or ""), determine the winner by checking all rows, columns, and both diagonals. 

# Input: [["X","X","X"],
#             ["O","O",""],
#             [" "," "," "]]
# Output: "X"

# def checkWiner(a):
#     for i in range(3):
#         if a[0][i] == a[1][i]== a[2][i]:
#             return a[0][i]
#         if a[i][0] == a[i][1] == a[i][2]:
#             return a[i][0]
#     if a[0][0] == a[1][1] == a[2][2]:
#         return a[0][0]
#     if a[2][0] == a[1][1] == a[0][2]:
#         return a[2][0]
#     return "Nothing....." 

# arr = [list(map(str, input().split(","))) for i in range(3)]
# print(arr)
# print(checkWiner(arr))

# ======================
# https://fcc.navgurukul.org/learn/project-euler/project-euler-problems-1-to-100/problem-6-sum-square-difference

# function sumSquareDifference(n) {
#   let sum = 0;
#   let sumOfAll = 0
#   for(let i =1; i <=n; i++){
#     sum+= i*i
#     sumOfAll += i
#   }
#   sumOfAll = sumOfAll ** 2
#   return (sumOfAll- sum)
# }

# sumSquareDifference(100);

# =======================================
