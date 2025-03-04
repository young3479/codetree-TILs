N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]

# print(info)

dp = [0] * 101 #1부터 담기

for s, e in info:
    for i in range(s, e+1):
        dp[i] += 1
        
print(max(dp))