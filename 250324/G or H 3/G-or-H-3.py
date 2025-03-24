n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

dp = [0] * (max(x)+1)

for i in range(n):
    if c[i] == 'G':
        dp[x[i]] += 1
    elif c[i] == 'H':
        dp[x[i]] += 2
        
ans = 0
for i in range(1, len(dp)-k+2):
    dist = 0
    dist = sum(dp[i:i+k+1])

    ans = max(dist, ans)

print(ans)


