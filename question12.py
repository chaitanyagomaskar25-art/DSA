# Find factorial of N. (Input: N = 5 | Output: 120)


n = int(input())

f = 1
for i in range(2, n+1):
    f*=i

print(f)
