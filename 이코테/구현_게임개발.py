# blog link:

n, m = map(int, input().split())

# 방문 위치를 저장하기 위한 맵 생성 & 0으로 초기화
d = [[0] * m for _ in range(n)]
# current X,Y, direction
x, y, direction = map(int, input().split())
d[x][y] = 1  # visited

# entire map info
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# turn left function


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# start simulation
count = 1
turn_time = 0

while True:
    turn_left()  # 항상 왼쪽으로 돈다.
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재 || 육지인 경우 -> 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1  # visited
        x = nx
        y = ny
        count += 1
        turn_time = 0  # init
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 || 바다인 경우
    else:
        turn_time += 1  # 회전수 +1

    # 네 방향 모두 막혀 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있으면 이동하기(nx,ny값을 x,y에 update)
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다라서 갈 수 없음
        else:
            break
        turn_time = 0
print(count)
