# Least Common Multiple (LCM) of two numbers. (Input: a = 4, b = 6 | Output: 12)


a = int(input())
b = int(input())
g = 1
for i in range(1, min(a+1, b+1)):
    if a % i == 0 and b % i == 0:
        g = i
print((a*b)//g)
