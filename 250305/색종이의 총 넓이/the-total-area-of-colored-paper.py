N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 201 for _ in range(201)]

for s, e in info:
    for i in range(s, s+8):
        for j in range(e, e+8):
            dp[i][j] = 1

#dp가 1인 부분 출력하기
cnt = 0
for x in range(201):
    for y in range(201):
        if dp[x][y] == 1:
            cnt += 1 
print(cnt)