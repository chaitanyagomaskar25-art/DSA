# Q1: Find the Key with the Maximum Value
# Given a dictionary of item names and their prices, find which key has the highest value. 

# INPUT: {"apple": 30, "banana": 50, "mango": 45}
# OUTPUT: "banana"

# n= int(input("Enter No. of object items: "))
# obj = {}
# for i in range(n):
#     key = input(f"Enter the {i+1} key: ")
#     value = int(input(f"Enter the value for {i+1} key: "))
#     obj[key] = value

# m = 0
# mKey = ""
# for i in obj:
#     if obj[i] > m:
#         m = obj[i]
#         mKey = i
# print(mKey)

# ============================================

# Q3: Find Both Min and Max (Multiple Return Values)
# Write a function that returns both the smallest and the largest number in a list at once.

# INPUT: [4, 2, 9, 1, 7]
# OUTPUT: (1, 9) 

# def get_min_max(a):
#     max = a[0]
#     min  = a[0]
    
#     for i in a:
#         if i > max:
#             max = i
#         if i < min:
#             min = i
#     return (min, max)

# print(get_min_max(list(map(int, input().split()))))

# ==================================

# Q4: Contains Duplicate Within K Distance 📏
# Given an array and a number k, check if there are two equal elements whose indices are at most k apart.

# Input: [1,2,3,1], k=3
# Output: True   (both 1s are within 3 positions of each other)
# Input: [1,2,3,1,2,3], k=2
# Output: False   (the repeated values are all more than 2 apart)

a = list(map(int, input().split()))
k = int(input())
isExist = False
for i in range(len(a)):
    m = k+i+1
    if m > len(a):
        m = len(a)
    for j in range(i+1, m):
        if a[i] == a[j]:
            print(True)
            isExist = True
            break
    if isExist:
        break
else:
    print(False)