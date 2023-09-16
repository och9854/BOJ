# import sys

# n = int(input())
# xs = list(map(int, sys.stdin.readline().split()))
# xs2 = sorted(list(set(xs)))

# dic = {}
# for i in range(len(xs2)):
#     dic[xs2[i]] = i

# for j in xs:
#     print(dic[j], end=' ')
input()
crd = list(map(int, input().split()))
idx = list(sorted(set(crd)))
dic = {c: i for i, c in enumerate(idx)}
# print(*(dic[c] for c in crd))
print(*(dic[c] for c in crd))
