# Full pyramid star pattern of height N. (Input: N = 3 | Output:   *   \n  ***  \n ***** )



n = int(input())

for i in range(1, n+1):
    spaces = (n - i) * ' '
    stars = ((2*i)-1) * "*"
    print(spaces+stars)
