N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N 

answer = 0
for x in range(N):
    for y in range(N):
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny):
                continue

            if info[nx][ny] == 1:
                cnt += 1

        if cnt >= 3:
            answer += 1
            
print(answer)