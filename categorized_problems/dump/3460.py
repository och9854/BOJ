t = int(input())
arr = [int(input()) for i in range(t)]


def decTobi(num: int) -> int:
    if num == 1:
        return 1

    res = ""
    while True:
        remain = num % 2
        num = num // 2
        res += str(remain)
        if num == 1:
            res += '1'
            break
    return int(res[::-1])


def printOne(num: int) -> None:
    string = str(num)[::-1]
    # loop and check 1
    for idx, i in enumerate(string):
        if i == '1':
            print(idx, end=' ')
    print()
    return None


for num in arr:

    printOne(decTobi(num))
