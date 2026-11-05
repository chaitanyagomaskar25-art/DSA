# Diamond star pattern of height 2N-1. (Input: N = 3 | Output:   *   \n  ***  \n ***** \n  ***  \n   *   )

n = int(input())

for i in range(1, n+1):
    spaces = (n - i) * ' '
    stars = ((2*i)-1) * "*"
    print(spaces+stars)

for i in range(n-1, 0, -1):
    spaces = (n - i) * " "
    stars = ((2*i)-1) * "*"
    print(spaces+stars)

