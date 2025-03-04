N = int(input())
info = [list(input().split()) for _ in range(N)]

dx = [1, 0, -1, 0] #동, 남, 서, 북 
dy = [0, -1, 0, 1]

x, y = 0, 0
direct = 0

for i in range(N): 
    if info[i][0] == 'E': 
        direct = 0
    elif info[i][0] == 'S':
        direct = 1
    elif info[i][0] == 'W':
        direct = 2
    else: 
        direct = 3

    if direct == 1 or direct == 3: #Y가 움직인 경우
        x, y = x, (y + (int(info[i][1]) * dy[direct]))
    else: #X가 움직인 경우
        x, y = (x + (int(info[i][1]) * dx[direct])), y

print(x, y)





