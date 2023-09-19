s = input()
ans = []
for i in range(len(s)):  # repeat n times
    ans.append(s[i:])

print('\n'.join(sorted(ans)))
# ans = sorted(ans)
# for i in ans:
#     print(i)
