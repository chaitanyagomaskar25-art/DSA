# n= int(input("Enter a number: "))

# for i in range(n, 0, -1):
#     rows = i * 2 - 1
#     spaces = n-i
#     print((spaces * " ") + (rows*"*"))

# for i in range(2, n + 1):
#     rows = i * 2 - 1
#     spaces = n - i
#     print((spaces * " ") + (rows * "*"))


# with spaces

# n = 5
# for i in range(1,n+1):
#     row = " ".join(str(j) for j in range(1, i+1))
#     if i > 1:
#         row += " " + " ".join(str(j) for j in range(i-1, 0, -1))
#     spaces = (n - i) *2
#     print((spaces * " " ) + row)


# without spaces
# n = 5
# for i in range(1,n+1):
#     row = "".join(str(j) for j in range(1, i+1))
#     row += "".join(str(j) for j in range(i-1, 0, -1))
#     spaces = n - i
#     print((spaces * " " ) + row)