N, M = map(int, input().split())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
direct = 1

info = [[0] * M for _ in range(N)]

def in_range(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

for i in range(1, N*M + 1):
    info[x][y] = i

    nx = x + dx[direct]
    ny = y + dy[direct]

    if not in_range(nx, ny) or info[nx][ny] != 0:
        #벽에 부딪힐 때마다 방향 바꿔야함 & 안쪽으로 들어가야함
        direct = (direct + 3) % 4
    
    x = x + dx[direct]
    y = y + dy[direct]
    
for i in range(N):
    for j in range(M):
        print(info[i][j], end=' ')
    print()