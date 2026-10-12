# 1. Sum of all elements

# Given [[1, 2, 3], [4, 5, 6]], return the sum of all elements.
# Target: O(R × C) time, O(1) extra space.

# a = [[1,2,3],[4,5,6]]
# s = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         s+=a[i][j]

# print(s)

# ===================================================
# 2. Row sums

# Given [[1, 2, 3], [4, 5, 6], [7, 8, 9]], return [6, 15, 24].
# Target: O(R × C) time, O(R) output space.


# a = [[1,2,3],[4,5,6],[7,8,9]]

# s = []
# for i in range(len(a)):
#     sum = 0
#     for j in range(len(a[i])):
#         sum+=a[i][j]
#     s.append(sum)

# print(s)


# ====================================================
# 3. Main and secondary diagonals

# For a 3 × 3 matrix, calculate both diagonal sums. For [[1,2,3],[4,5,6],[7,8,9]], they are 15 and 15.
# Target: O(N) time, O(1) extra space.




# a = [[1,2,3],[4,5,6],[7,8,9]]
# s1 = 0
# s2 = 0

# for i in range(len(a)):
#     s1+=a[i][i]
#     s2+=a[i][len(a)-i-1]

# print(s1,s2)

# ========================================

# 4. Count even numbers

# Given [[1, 2, 4], [5, 6, 7]], count how many elements are even.
# Target: O(R × C) time, O(1) extra space.

# a = [[1,2,4],[5,6,7]]
# c = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j] % 2 == 0:
#             c+=1

# print(c)


# ======================================

# 5. Transpose a matrix

# Convert [[1, 2, 3], [4, 5, 6]] into [[1, 4], [2, 5], [3, 6]].
# Target: O(R × C) time, O(R × C) output space.

# a = [[1,2,3],[4,5,6]]

# rows = len(a)
# cols = len(a[0])
# transpose = []
# for c in range(cols):
#     newArr = []
#     for r in range(rows):
#         newArr.append(a[r][c])
#     transpose.append(newArr)

# print(transpose)



# ================================

# 6. Rotate 90° clockwise

# Rotate [[1, 2, 3], [4, 5, 6], [7, 8, 9]] in place.
# Target: O(N²) time, O(1) auxiliary space.



# a = [[1,2,3],[4,5,6],[7,8,9]]

# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         a[i][j], a[j][i] = (a[j][i], a[i][j])

# for i in range(len(a)):
#     a[i].reverse()

# print(a)
    

# ========================

# 7. Search a sorted matrix

# Search for 13 in [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]. Return True if found.
# Target: O(R + C) time, O(1) extra space.
          
# a = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]

# target = 13
# rows = len(a)
# cols = len(a[0])

# r = 0
# c = cols-1

# while r < rows and c >=0:
#     if a[r][c] == target:
#         print("Founded", a[r][c], "=>", (r,c))
#         break
#     elif a[r][c] > target:
#         c-=1
#     else:
#         r+=1

# ============================================


# Spiral traversal

# Return all elements of a rectangular matrix in clockwise spiral order.
# Target: O(R × C) time, O(R × C) output space.

# a = [[1,2,3],[4,5,6],[7,8,9]]
# top = 0
# bottom = len(a)-1
# left = 0
# right = len(a[0])-1

# while top<=bottom and left<=right:
#     # left=>right
#     for i in range(left, right+1):
#         print(a[top][i], end=" ")
#     top+=1

#     # top=>bottom
#     for i in range(top, bottom+1):
#         print(a[i][right], end=" ")
#     right-=1

#     # right=>left
#     if top <= bottom:
#         for i in range(right, left-1,-1):
#             print(a[bottom][i], end=" ")
#         bottom-=1
    
#     # bottom=>top
#     if left<=right:
#         for i in range(bottom, top-1, -1):
#             print(a[i][left], end=" ")
#         left+=1

# print()