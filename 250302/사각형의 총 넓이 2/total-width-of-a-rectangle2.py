N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

# 1이상인 부분 체크
rect = [[0] * 210 for _ in range(210)]

for x1, y1, x2, y2 in info:
    for i in range(x1, x2):
        for j in range(y1, y2):
            rect[i][j] = 1

cnt = 0
for i in range(210):
    for j in range(210):
        if rect[i][j] == 1:
            cnt += 1
    
print(cnt)