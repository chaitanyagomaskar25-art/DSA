# Sort array of 0s, 1s, and 2s (Dutch National Flag). (Input: [2, 0, 2, 1, 1, 0] | Output: [0, 0, 1, 1, 2, 2])


# a = list(map(int, input().split()))

# l = 0
# r = len(a)-1

# while l<=r:
#     m = (l+r)//2
#     if a[m] == 0:
#         a[l],a[m] = a[m],a[l]
#         l+=1
#     elif a[m] == 2:
#         a[r], a[m] = a[m],a[r]
#         r-=1
#     else:
#         l+=1
#         r-=1
# print(a)

