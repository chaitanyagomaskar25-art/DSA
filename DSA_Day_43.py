# 1. Linear search

# Given arr = [4, 8, 12, 16, 20], return the index of target 16. Return -1 if it is absent.


# arr = [4,8,12,16,20]
# target = 12

# for i, value in enumerate(arr):
#     if value == target:
#         print("founded", i, value)
#         break
# else:
#     print("Not found", -1)


# ===================================
# 3. Find all occurrences

# Given arr = [2, 5, 2, 7, 2, 9], return all indices where target 2 occurs.


# arr = [2, 5, 2, 7, 2, 9]
# target = 2

# indices = []
# for i, v in enumerate(arr):
#     if v == target:
#         indices.append(i)

# print(indices)

# ==================================================

# 4. Binary search

# Implement iterative binary search for arr = [3, 7, 11, 15, 19, 23, 27]. Find target 19 and return its index.

# arr = [3, 7, 11, 15, 19, 23, 27]
# target = 19

# left = 0
# right = len(arr) -1

# while left<=right:
#     mid = (left+right) //2
#     if arr[mid] == target:
#         print(mid)
#         break
#     elif arr[mid] < target:
#         left = mid+1
#     else:
#         right = mid-1



# =========================================================


# 5. First and last occurrence

# Given the sorted list [1, 2, 2, 2, 3, 4, 4, 5], find the first and last index of target 2.


# arr = [1, 2, 2, 2, 3, 4, 4, 5]
# target = 2
# indices = []
# for i, v in enumerate(arr):
#     if v == target:
#         indices.append(i)

# if indices:
#     print(indices[0], indices[-1])
# else:
#     print(-1, -1)

# =======================================


# 6. Count occurrences

# Count how many times target 6 occurs in [6, 1, 6, 3, 6, 8, 2]. Solve it in O(n) time.

# arr = [6, 1, 6, 3, 6, 8, 2]
# target = 6
# c = 0

# for i, v in enumerate(arr):
#     if v == target:
#         c+=1

# print(c)


# ====================================

# 7. Search insert position

# Given the sorted list [1, 3, 5, 7], return the index where target 6 should be inserted to keep the list sorted. Use binary search in O(log n) time.

# arr =[1, 3, 5, 7]
# target = 8

# l = 0
# r = len(arr)-1
# while l<=r:
#     mid = (l+r)//2
#     if arr[mid] == target:
#         print(mid)
#         break
#     elif arr[mid] < target:
#         l = mid+1
#     else:
#         r = mid-1
# else:
#     print(l)


# ========================================

# 8. Search in a rotated sorted list

# Given [7, 9, 12, 1, 3, 5], find target 3 in O(log n) time. Return its index, or -1 if absent.
# arr = [7, 9, 12, 1, 3, 5]
# target = 9
# l = 0
# r = len(arr)-1


# while l <=r:
#     mid = (l+r)//2

#     if arr[mid] == target:
#         print(mid)
#         break
#     elif arr[l] < arr[mid]:
#         if arr[l] <= target < arr[mid]:
#             r = mid-1
#         else:
#             l = mid+1
#     else:
#         if arr[mid] < target <= arr[r]:
#             l = mid+1
#         else:
#             r = mid-1


