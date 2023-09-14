a, b, v = map(int, input().split())
# A: up, B: down, V: top
# if the snail can reach during the day at the last day +0 else +1
print((v-b)//(a-b) if (v-b) % (a-b) == 0 else (v-b)//(a-b)+1)
