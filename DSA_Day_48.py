# *****
# *****
# *****
# *****
# *****

# n = int(input())
# for i in range(n):
#     s = n * "*"
#     print(s)


# ===============================

# *
# **
# ***
# ****
# *****
# n = int(input())

# for i in range(1, n+1):
#     s = i * "*"
#     print(s)


# =====================

# *****
# ****
# ***
# **
# *
# n = int(input())

# for i in range(n, 0, -1):
#     s = i * "*"
#     print(s)


# ====================

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# n = int(input())

# for i in range(1, n+1):
#     s = ""
#     for j in range(1,i+1):
#         s += " " + str(j)
#     print(s.strip())


# ============================

# 1
# 22
# 333
# 4444
# 55555

# n = int(input())

# for i in range(1, n+1):
#     s = str(i) * i 
#     print(s)


# ===============================

# 1
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
# n = int(input())

# c = 1
# for i in range(n):
#     s = ""
#     for j in range(i+1):
#         s += str(c) + " "
#         c+=1
#     print(s)



# ===============================
#     *
#    **
#   ***
#  ****
# *****
# n = int(input())


# for i in range(1, n+1):
#     s = i * "*"
#     spaces = (n-i) * " "
#     print(spaces + s)



# ===============================

#     *
#    ***
#   *****
#  *******
# *********

# n = int(input())


# for i in range(1, n + 1):
#     starts = i * 2 - 1
#     spaces = n - i
#     print((spaces * " ") + (starts * "*"))


# ===============================

# *********
#  *******
#   *****
#    ***
#     *
# n = int(input())

# for i in range(n , 0, -1):
#     starts = i * 2 - 1
#     spaces = n- i
#     print((spaces * " ")+ (starts * "*"))


# ===============================

# * * * * *
# *       *
# *       *
# *       *
# * * * * *
# n = int(input())

# for i in range(1, n+1):
#     if i == 1 or i == n:
#         # stars = n * "*"
#         stars = " ".join("*" for j in range(n))
#         print(stars)
#     else:
#         stars = "*"
#         # spaces = (n-2) * " "
#         spaces = " ".join(" " for j in range(n-1))
#         print(stars + spaces + stars) 


# # ===============================

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# n = int(input())

# for i in range(1, n):
#     stars = i * 2 -1
#     spaces = n - i
#     print((spaces * " ") + (stars * "*"))

# for i in range(n, 0, -1):
#     stars = i * 2 -1
#     spaces = n - i
#     print((spaces * " ") + (stars * "*"))
    
    
# ===============================

# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

# n = int(input())


# for i in range(n, 0, -1):
#     stars = i * 2 -1
#     spaces = n - i
#     print((spaces * " ") + (stars * "*"))
    


# for i in range(2, n+1):
#     stars = i * 2 -1
#     spaces = n - i
#     print((spaces * " ") + (stars * "*"))


# ===============================

# 1
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1 

# n = int(input())


# for i in range(1, n+1):
#     s = ""
#     for j in range(1, i+1):
#         if i % 2 == 0:
#             if j % 2 == 0:
#                 s += "1 "
#             else:
#                 s += "0 "
#         else:
#             if j % 2 == 0:
#                 s += "0 "
#             else:
#                 s += "1 "
#     print(s)



# ===============================


# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# n = int(input())

# for i in range(1, n):
#     stars = i * "*"
#     spaces = ((2* n) - (i *2)) * " "
#     print(stars + spaces + stars) 

# for i in range(n, 0, -1):
#     stars = i * "*"
#     spaces = ((2* n) - (i *2)) * " "
#     print(stars + spaces + stars)

# ==================================


#      1
#     1 2
#    1 2 3
#   1 2 3 4
#  1 2 3 4 5

# n = int(input())

# for i in range(1, n+1):
#     row = " ".join(str(j) for j in range(1, i+1))
#     spaces = (n - i) * " "
#     print(spaces, row)


# ============================================

#      1
#     121
#    12321
#   1234321
#  123454321

# n = int(input())

# for i in range(1, n+1):
#     row = "".join(str(j) for j in range(1, i+1))
#     nextRow = "".join(str(j) for j in range(i-1, 0, -1))
#     spaces = (n - i) * " "
#     print(spaces, row + nextRow)


# ===================

#      1
#     121
#    12312
#   1234123
#  123451234

# n = int(input())

# for i in range(1, n+1):
#     row = "".join(str(j) for j in range(1, i+1))
#     nextRow = "".join(str(j) for j in range(1, i))
#     spaces = (n - i) * " "
#     print(spaces, row + nextRow)


# ===============

