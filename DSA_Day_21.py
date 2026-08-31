#Sort 0s and 1s
# Input
# 8
# 0 1 1 0 1 0 0 1
# Output
# 0 0 0 0 1 1 1 1

# n = int(input())
# a = list(map(int, input().split())) 
# s =0 
# for i in range( n):
#     if a[i] !=1:
#         a[s],a[i] = a[i], a[s]
#         s+=1
# print(a)


# ======================================
# Generate All Permutations
# Input
# abc
# Output
# abc
# acb
# bac
# bca
# cab
# cba

# def permutation(a):
#     if len(a) <= 1:
#         return [a]
#     result = [] 
#     for i, char in enumerate(a):
#         ans = a[:i]+a[i+1:] 
#         for j in permutation(ans):
#             result.append(char+j)
          
#     return result

# print('\n'.join(permutation(input())))

# =================================


