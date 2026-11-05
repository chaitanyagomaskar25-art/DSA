# Count digits in an integer. (Input: N = 54321 | Output: 5)


n = int(input())

c = 0
while n > 0:
    c+=1
    n = n//10

print(c)