# Sum of first N natural numbers. (Input: N = 5 | Output: 15)



n = int(input())
s = 0
for i in range(1, n+1):
    s+=i

print(s)
