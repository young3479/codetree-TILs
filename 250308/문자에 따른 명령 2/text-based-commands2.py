info = list(input())

dx = [1, 0, -1, 1]
dy = [0, -1, 0, 1]

direct = 3
x, y = 0, 0

for i in info:
    if i == 'L': #왼쪽으로 90도 회전
        direct = (direct + 3) % 4 
    elif i == 'R': #오른쪽으로 90도 회전
        direct = (direct + 1) % 4 
    else: #바라보는 방향으로 한칸 직진
        x = x + dx[direct]
        y = y + dy[direct]

print(x, y)
