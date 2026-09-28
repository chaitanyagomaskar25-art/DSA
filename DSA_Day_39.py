# 1 2 3 4 5

# 5 4 3 2 1

# 1 2 3 4 5

# 5 4 3 2 1


# Depend on N = ?


# a = [[1,2,3,4,5],[5,4,3,2,1],[1,2,3,4,5],[5,4,3,2,1]]
# print(len(a[0]))


# =================================================

# 1
# 1 2
# 1    3
# 1       4
# 1 2  3  4  5

# n = int(input())

# for i in range(n):
#     s =""
#     for j in range(i+1):
#         if i == n-1:
#             s+= str(j+1)
#         elif j == 0 or j == (i):
#             s+= str(j+1)
#         else:
#             s+= " "
#     print(s)


# =============================================

# A shop provides discounts:

# Purchase Amount   Discount
# Below 
# ₹1,000                 No discount
# ₹1,000–₹4,999       5%
# ₹5,000–₹9,999       10%
# ₹10,000 or more     15%

# Calculate the final amount.

# Test Cases
# Amount
# Expected Final Amount
# ₹500
# ₹500
# ₹1,000
# ₹950
# ₹5,000
# ₹4,500
# ₹10,000
# ₹8,500
# ₹20,000
# ₹17,000


# a = int(input("Enter an amount: "))
# if a < 1000:
#     print(f"₹{a}")
# elif a < 5000:
#     print(f'₹{int(a- (a*5/100))}')
# elif a < 10000:
#     print(f'₹{int(a-(a*10/100))}')
# else:
#     print(f'₹{int(a-(a*15/100))}')