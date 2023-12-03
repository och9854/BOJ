s = input().replace("()", "-")
c, p = 0, 0
for i in s:
    if i == '-':
        p += c
    elif i == '(':
        c, p = c+1, p+1
    else:
        c -= 1
print(p)
