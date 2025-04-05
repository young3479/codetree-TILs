n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = -1
# 하나씩 돌면서 거기서 3x3을 잡기
for i in range(n):
    for j in range(n):
        # 범위가 넘지 않는 거 체크
        if i+2 > n-1 or j+2 > n-1:
            continue
        # 범위내라면 3x3에서 코인의 개수 세기
        coin = 0 
        for x in range(i, i+3):
            for y in range(j, j+3):
                if grid[x][y] == 1:
                    coin += 1
        
        ans = max(coin, ans)
        
print(ans)