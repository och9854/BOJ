n = int(input())
ans = ""
if n == 0:
    print('0')
    exit()
while n:
    if n % (-2):
        ans += '1'
        n = n//(-2) + 1
    else:
        ans += '0'
        n //= -2

print(int(ans[::-1]))
