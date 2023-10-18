import itertools
import sys
arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline()))
'''
9C2 번의 연산을 진행해야 함
1 3번 난쟁이가 아닐 경우 -> 둘을 제외하고 100

전체 9명의 합을 계산하고, 거기서 둘둘씩 빼서 합이 100이 되면 종료

arr[1] 빼기, arr[2],...arr[9] 빼기
arr[2] 빼기, arr[1],...arr[9] 빼기

'''

for i in itertools.combinations(arr, 7):  # 9C7
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        exit()
