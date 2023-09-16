l = []
for _ in range(5):
    l.append(int(input()))

l.sort()

print(f'{int(sum(l)/5)}\n{l[2]}')
