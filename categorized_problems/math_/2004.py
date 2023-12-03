import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def count_t(n, t):
    if n < t:
        return 0
    count = 0
    while n >= t:
        count += n//t
        n = n//t

    return count


two_cnt = count_t(n, 2)-count_t(n-m, 2)-count_t(m, 2)
five_cnt = count_t(n, 5)-count_t(n-m, 5)-count_t(m, 5)
print(min(two_cnt, five_cnt))
