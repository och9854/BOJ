from itertools import combinations, permutations

n = int(input())
arr = list(map(int, input().split()))
ops = list(map(int, input().split()))
ops = ''.join(['+', '-', '*', '%'][idx]*op for idx, op in enumerate(ops))
perms = []
for i in list(permutations(ops, n-1)):
    perms.append(''.join(list(i)))

perms = list(set(perms))

res = []
for i in perms:
    temp = arr[0]
    for idx, j in enumerate(i):
        if j == '%':
            j = '/'
        temp = int(eval(str(temp) + j + str(arr[idx+1])))
        # if j == '/' and temp < 0:
        #     temp += 1

    res.append(temp)


print(max(res))
print(min(res))
