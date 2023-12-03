import sys


def check(s):
    cnt = [0, 0, 0, 0]  # lower, upper, num, space
    for i in s:
        if ord('a') <= ord(i) <= ord('z'):  # alpha lower
            cnt[0] += 1
        elif ord('A') <= ord(i) <= ord('Z'):  # alpha upper
            cnt[1] += 1
        elif ord('0') <= ord(i) <= ord('9'):  # num
            cnt[2] += 1
        else:  # space
            cnt[3] += 1
    print(*cnt)


while True:
    string = sys.stdin.readline()[:-1]
    if string == "":
        break
    else:
        check(string)
