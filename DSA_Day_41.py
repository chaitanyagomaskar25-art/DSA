# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
# Do with normal list


# n = int(input("Enter number of rows: "))
# a = [list(map(int, input().split())) for _ in range(n)]

# print(a)
# r = []
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         r.append(a[i][j])

# print(r)

# ================================================

# 1. Naive String Matching (Brute Force)

# a = [1,2,3,1,2,3,4,5]
# s = [1,2,3]

# m = len(s)
# n = len(a)

# maxRange = n-m+1

# for i in range(maxRange):
#     isMatching = True
#     j = 0
#     while j < m and isMatching == True:
#         if s[j] != a[i+j]:
#             isMatching = False
#         j+=1
#     if isMatching:
#         print(i)


# =============================================

# 2. Knuth-Morris-Pratt (KMP) Algorithm 



# def find_lps(p):
#     m = len(p)
#     lps = [0] * m
#     length = 0
#     i = 1

#     while i < m:
#         if p[length] == p[i]:
#             length +=1
#             lps[i] = length
#             i+=1
#         else:
#             if length !=0:
#                 length = lps[length-1]
#             else:
#                 lps[i] = 0
#                 i+=1
#     return lps


# def find_pattern(s,p):
#     if p == "":
#         return 0
    
#     lps = find_lps(p)

#     i = 0
#     j = 0
#     while i < len(s):

#         if s[i] == p[j]:
#             i+=1
#             j+=1

#             if j == len(p):
#                 return i - j
            
#         else:
#             if j!=0:
#                 j = lps[j - 1]
#             else:
#                 i+=1
#     return -1


# s = "babababacababcabab"
# p = "ababcabab"

# print(find_pattern(s, p))
# print(find_lps(p))


# =======================================

