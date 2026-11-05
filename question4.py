# Sum of all even numbers from 1 to N. (Input: N = 6 | Output: 12)

n = int(input())

s = 0
for i in range(2, n+1, 2):
    s+=i

print(s)