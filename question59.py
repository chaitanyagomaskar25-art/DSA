# Separate even and odd numbers in array. (Input: [1, 2, 3, 4, 5, 6] | Output: [2, 4, 6, 1, 3, 5])



# a = list(map(int, input().split()))
# odd = []
# even = []

# for i in a:
#     if i % 2 ==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even+odd)


# or

# r = len(a)-1
# l = 0

# while l<=r:
#     m = (l+r)//2
#     if a[m] % 2 == 0:
#         a[l],a[m]=a[m],a[l]
#         l+=1
#     else:
#         a[r],a[m]=a[m],a[r]
#         r-=1

# print(a)