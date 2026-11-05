# Segregate 0s and 1s. (Input: [0, 1, 1, 0, 1, 0] | Output: [0, 0, 0, 1, 1, 1])


# a = list(map(int, input().split()))


# l = 0
# r = len(a)-1
# while l<=r:
#     m=(l+r)//2
#     if a[m]% 2 ==0:
#         a[l],a[m] = a[m],a[l]
#         l+=1
#     else:
#         a[r],a[m] = a[m],a[r]
#         r-=1
# print(a)
