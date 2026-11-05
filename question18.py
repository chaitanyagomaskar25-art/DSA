# Check if a number is a Perfect Number. (Input: N = 6 | Output: true (1 + 2 + 3 = 6))



n = int(input())

s = 0
for i in range(1, n):
    if n % i == 0:
        s+=i

if n == s:
    print(True)
else:
    print(False)