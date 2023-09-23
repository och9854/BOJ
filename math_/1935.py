import math
n = int(input())


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcd(nums: list):
    a = nums[0]
    b = nums[1]
    print(int(a*b / gcd(a, b)))


for i in range(n):
    lcd(list(map(int, input().split())))
