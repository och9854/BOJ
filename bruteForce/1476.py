a1, a2, a3 = map(int, input().split())  # 1~15, 1~28, 1~19
c1, c2, c3 = 1, 1, 1
cnt = 1
while True:
    if a1 == c1 and a2 == c2 and a3 == c3:
        print(cnt)
        break
    else:
        # cnt
        cnt += 1
        # sum
        c1 += 1
        c2 += 1
        c3 += 1
        # rebalance
        if c1 == 16:
            c1 -= 15
        if c2 == 29:
            c2 -= 28
        if c3 == 20:
            c3 -= 19
