# g4: https://www.acmicpc.net/problem/14719
# better code: https://bio-info.tistory.com/188
'''
- 좌, 우에는 빗물이 고일 수 없다는 점을 놓침
- 나는 아래에서 위로 한줄씩, 한 요소씩 체크했는데, 
다른 사람들은 해당 블록의 좌우를 기준으로 [가장 낮은 것] & [현재 블록 높이] 를 비교해 얼마나 찰지 세팅했다!
'''
from collections import Counter

# 1. Get Array
h, w = map(int, input().split())
arr = [[0 for i in range(w)] for i in range(h)]


ws = list(map(int, input().split()))  # 3 0 1 4
for idx, i in enumerate(ws):
    for j in range(0, h):
        if i > j:
            arr[j][idx] = 1


# 2. Sum Possible
res = 0

for i in arr:
    row = Counter(i)
    # no water
    if row[1] <= 1:
        break
    # calculate water between 1 indices
    else:
        min = i.index(1)
        max = w - 1 - i[::-1].index(1)
        for idx, j in enumerate(i):
            if j == 0 and min < idx < max:
                res += 1


print(res)


'''

4 8
3 1 2 3 4 1 1 2

'''
