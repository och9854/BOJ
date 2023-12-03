
from collections import Counter
from itertools import combinations
# g4: https://www.acmicpc.net/problem/1062
N, K = map(int, input().split())
words = [input() for _ in range(N)]  # words list#[4:-4]
base_string = "antic"  # ['a', 'n', 't', 'i', 'c']
num_string = 5
res = []
#
if K < 5:
    print(0)
    exit()
all_strings = ''.join(words)

counts = Counter(all_strings)
for i in base_string:
    del counts[i]

combs = combinations(counts, K-5)
print(*combs)
for comb in combs:
    cnt = 0
    string = base_string + ''.join(comb)
    # print(string)
    for word in words:
        # print(set(word) - set(string))
        if len(set(word) - set(string)) == 0:
            cnt += 1
    res.append(cnt)

print(max(res))
