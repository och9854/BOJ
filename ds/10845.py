from collections import deque
import sys
n = int(input())
queue = deque()


def oper(queue) -> None:
    string = sys.stdin.readline().split()

    if string[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            result = queue.popleft()
            print(result)
    elif string[0] == 'size':
        print(len(queue))
    elif string[0] == 'empty':
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    elif string[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif string[0] == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
    else:  # push

        queue.append(int(string[1]))


for i in range(n):
    # do operations
    oper(queue)
