n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))
d.reverse()
grid = [u, d]

# n개의 개수가 있는 두 줄짜리 컨베이어 벨트
# t초 후의 모습
# 제일 처음 값을 temp에 담고 하나씩 돌리기

while t>0:
    temp = grid[0][0]
    # grid[0][0]은 temp에 넣고
    # 마지막에 grid[0][1]에 temp를 넣음
    # 나머지는 i=0 일땐, j가 늘어나고 (단, [0][끝]일땐 i가 늘어남)
    # i=1 일땐, j가 줄어듬 (단, [1][처음]일땐 i가 줄어듬)
    for i in range(1, -1, -1): #1, 0
        if i == 1:
            for j in range(n):
                if j == 0:
                    grid[i-1][j] = grid[i][j]
                else:
                    grid[i][j-1] = grid[i][j]
        if i == 0:
            for j in range(n-1, -1, -1):
                if j == n-1:
                    grid[i+1][j] = grid[i][j]
                elif j == 1:
                    grid[i][j+1] = grid[i][j]
                elif j == 0:
                    grid[i][j+1] = temp
                    # grid[i-1][j] = grid[i][j] 
    t -= 1

grid[1].reverse()
for i in range(2):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()
