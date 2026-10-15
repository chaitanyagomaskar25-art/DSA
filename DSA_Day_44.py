# ====Interpolation search============================



# def interpolationSearch(a, target):
#     l = 0
#     r = len(a)-1

#     while l <= r and a[l] <= target <= a[r]:
#         if a[l] == a[r]:
#             if a[l] == target:
#                 return l
#             return -1

#         p = l + (((target - a[l]) * (r-l)) // (a[r]-a[l]) )

#         if a[p] == target:
#             return p
#         elif a[p] < target:
#             l = p+1
#         else:
#             r = p-1
#     return -1


# a = [10,20,30,40,50,60,70,80,90,100] 
# target = 40

# print(interpolationSearch(a, 91)) 


