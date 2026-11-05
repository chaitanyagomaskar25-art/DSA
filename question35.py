# Strong number check (sum of factorials of digits equals number). (Input: 145 | Output: true (1! + 4! + 5! = 145))



# n = int(input())
# num = n
# s = 0
# while n > 0:
#     d = n % 10
#     f = 1
#     for i in range(1,d+1):
#         f*=i
#     s+=f
#     n = n // 10

# if num == s:
#     print(True)
# else:
#     print(False