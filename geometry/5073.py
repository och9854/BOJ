

def check(a, b, c):
    # end
    if a == 0:
        return 0

    # not triangle
    if 2*max([a, b, c]) >= a+b+c:
        return "Invalid"

    # triangle
    if a == b and b == c:  # 3동일
        return "Equilateral"
    elif a == b or b == c or a == c:  # 2동일
        return "Isosceles"
    else:
        return "Scalene"


while 1:
    a, b, c = list(map(int, input().split()))
    result = check(a, b, c)
    if result == 0:
        break
    print(result)
