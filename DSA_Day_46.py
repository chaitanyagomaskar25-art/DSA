s = "()[]{}"
f = {}
for i in s:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)
for i in f:
    if f[i] % 2 !=0:
        print(False)
        break
else:
    print(True)