s = input()
counts = [-1]*26  # 26 alphas
for idx, i in enumerate(s):
    # string came at the first time
    if counts[ord(i) - ord('a')] == -1:
        counts[ord(i) - ord('a')] = idx


print(*counts)
