a, b, c = int(input()), int(input()), int(input())


def check(a, b, c):
    if a + b + c != 180:
        return "Error"
    elif a == 60 and b == 60:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


print(check(a, b, c))
