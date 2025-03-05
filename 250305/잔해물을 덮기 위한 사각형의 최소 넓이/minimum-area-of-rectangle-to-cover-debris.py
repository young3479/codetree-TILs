x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

dp = [[0]*2001 for _ in range(2001)]

for i in range(x1, x2):
    for j in range(y1, y2):
        dp[i][j] = 1

for i in range(a1, a2):
    for j in range(b1, b2):
        dp[i][j] = 0


# for x in range(2001):
#     for y in range(2001):
#         if dp[x][y] == 1:
#             print(x, y)


#가로 길이 2개중 더 큰것, 세로 길이 2개중 더 큰것 곱하기
min_x = 2001
max_x = 0
min_y = 2001
max_y = 0

for x in range(2001):
    for y in range(2001):
        if dp[x][y] == 1:
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

width = max_x - min_x + 1
height = max_y - min_y + 1


print(width * height) # 5 * 3 = 15