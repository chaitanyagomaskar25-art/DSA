# Reverse an integer. (Input: N = 1234 | Output: 4321)


n = int(input())

m = 0
while n > 0:
    d = n % 10
    m = d + (m*10)
    n = n//10
print(m)


