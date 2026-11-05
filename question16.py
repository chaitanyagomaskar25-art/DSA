# Print all prime numbers up to N. (Input: N = 15 | Output: 2, 3, 5, 7, 11, 13)


n = int(input())


for i in range(2, n+1):
    isPrime = True
    j = 2
    while isPrime and j < i:
        if j != i and i % j == 0 :
            isPrime = False
        j+=1
    if isPrime:
        print(j)