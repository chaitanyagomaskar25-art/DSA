# Check if a number is a Palindrome. (Input: N = 1221 | Output: true; Input: N = 123 | Output: false)



n = int(input())

s = str(n)

l =0 
r = len(s)-1
while l<=r:
    if s[l] != s[r]:
        print(False)
        break
    l+=1
    r-=1
else:
    print(True)