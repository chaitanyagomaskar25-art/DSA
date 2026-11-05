# Number triangle pattern (row i prints 1..i). (Input: N = 3 | Output: 1 \n 1 2 \n 1 2 3)



n = int(input())
for i in range(1, n+1):
    s = ""
    for j in range(1,i+1):
        s+=str(j)
    print(s)