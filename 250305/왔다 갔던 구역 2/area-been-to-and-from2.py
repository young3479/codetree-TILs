N = int(input())
info = [list(input().split()) for _ in range(N)]

dp = [0] * 1001

x = 0
cnt = 0
for i in range(N):
    info[i][0] = int(info[i][0])
    if info[i][1] == "R":
        for j in range(x, (x+info[i][0])):
            if dp[j] == 1:
                cnt += 1
            dp[j] += 1
        x += info[i][0]
    else:
        for j in range((x-info[i][0]), x):
            if dp[j] == 1:
                cnt += 1
            dp[j] += 1
        x -= info[i][0]

print(cnt)


