# Three Sum (triplets adding to 0). (Input: [-1, 0, 1, 2, -1, -4] | Output: [[-1, -1, 2], [-1, 0, 1]])



# a = list(map(int, input().split()))
# result = []
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         for k in range(j+1, len(a)):
#             if (a[i]+a[j]+a[k]) == 0:
#                 s = sorted([a[i],a[j],a[k]])
#                 if s not in result:
#                     result.append(s)
# print(result) 