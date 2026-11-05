# Check if a number is Prime. (Input: N = 17 | Output: Prime; Input: N = 15 | Output: Not Prime)

n = int(input())

isPrime = True

i = 2
while isPrime and i < n:
    if i != n and n % i == 0 :
        isPrime = False
    i+=1

if isPrime:
    print("Yes")
else:
    print("No")


