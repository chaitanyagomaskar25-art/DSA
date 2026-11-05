# Inverted right triangle pattern of height N. (Input: N = 3 | Output: *** \n ** \n *)


n = int(input())

for i in range(n, 0, -1):
    s = i *"*"
    print(s)