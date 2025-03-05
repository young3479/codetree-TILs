x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

dp = [[0]*2001 for _ in range(2001)]

for i in range(x1, x2):
    for j in range(y1, y2):
        dp[i][j] = 1

for i in range(a1, a2):
    for j in range(b1, b2):
        dp[i][j] = 0

# cnt = 0
# for x in range(2001):
#     for y in range(2001):
#         if dp[x][y] == 1:
#             print(x, y)
#             cnt += 1

#가로 길이 2개중 더 큰것, 세로 길이 2개중 더 큰것 곱하기
min_x, max_x = 2001, -1
min_y, max_y = 2001, -1

for i in range(2001):
    for j in range(2001):
        if dp[i][j] == 1:
            if i < min_x:
                min_x = i
            if i > max_x:
                max_x = i
            if j < min_y:
                min_y = j
            if j > max_y:
                max_y = j

# 경계값들을 통해 사각형의 가로·세로 길이 계산
width = (max_x - min_x + 1)
height = (max_y - min_y + 1)

red_area = width * height
print(red_area)
