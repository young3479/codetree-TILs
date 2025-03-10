N = int(input())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = N//2, N//2
direct = 0

info = [[0] * N for _ in range(N)]

def in_range(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

for i in range(1, N*N+1):
    info[x][y] = i

    nx = x + dx[direct]
    ny = y + dy[direct]

    if not in_range(nx,ny) or info[nx][ny] != 0:
        direct = (direct + 3) % 4

    x = x + dx[direct]
    y = y + dy[direct]


for i in range(N):
    for j in range(N):
        print(info[i][j], end=' ')
    print()
