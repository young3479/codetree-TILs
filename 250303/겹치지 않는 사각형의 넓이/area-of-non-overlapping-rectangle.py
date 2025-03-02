x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

mx1, my1, mx2, my2 = map(int, input().split())

rect = [[0] * 2001 for _ in range(2001)]

for i in range(x1, x2):
    for j in range(y1, y2):
        rect[i][j] = 1

for i in range(x3, x4):
    for j in range(y3, y4):
        rect[i][j] = 1

for i in range(mx1, mx2):
    for j in range(my1, my2):
        rect[i][j] = 0

cnt = 0
for x in range(2001):
    for y in range(2001):
        if rect[x][y] == 1:
            cnt += 1

print(cnt)