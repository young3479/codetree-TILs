N, M = map(int, input().split())

#좌표는 이렇게 이동
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

info = [[0] * M for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

x, y = 0, 0
direct = 0

for i in range(1, N*M+1):
    info[x][y] = i

    nx = x + dx[direct]
    ny = y + dy[direct]

    # 범위가 아니거나 이미 지난 부분이면 방향을 바꾸기
    if not in_range(nx, ny) or info[nx][ny] != 0:
        direct = (direct + 1) % 4

    x = x + dx[direct]
    y = y + dy[direct]

for i in range(N):
    for j in range(M):
        print(info[i][j], end=" ")
    print()