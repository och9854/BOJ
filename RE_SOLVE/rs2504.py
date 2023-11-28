# g5: https://www.acmicpc.net/problem/2504
# ref: https://aigong.tistory.com/518
# ref: https://westernriver.tistory.com/7
# 아이디어 이해가 정말 어려웠다. 안에서부터 탐색하게 되는데, 이게 아니라
# 관련 설명 정리해서 블로그 올리기 상세설명 붙이기
import sys
input = sys.stdin.readline().rstrip()

list = []
isAns = True
val = 1
ans = 0

for i, str in enumerate(input):
    if str == "(":
        list.append(str)
        val *= 2

    elif str == "[":
        list.append(str)
        val *= 3

    elif str == ")":
        if not list or list[len(list) - 1] == "[":
            isAns = False
            break
        if input[i-1] == "(":
            ans += val
            print('done', val, ans, list)

        list.pop()
        val //= 2

    elif str == "]":
        if not list or list[len(list) - 1] == "(":
            isAns = False
            break
        if input[i-1] == "[":
            ans += val
            print('done', val, ans, list)
        list.pop()
        val //= 3

if not isAns or list:
    print(0)
else:
    print(ans)
