# Greatest Common Divisor (GCD) of two numbers. (Input: a = 12, b = 18 | Output: 6)

a = int(input())
b = int(input())
g = 1
for i in range(1, min(a+1, b+1)):
    if a % i == 0 and b % i == 0:
        g = i
print(g)
