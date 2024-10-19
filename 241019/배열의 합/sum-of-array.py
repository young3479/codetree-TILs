map = [list(map(int, input().split())) for _ in range(4)]
answer = 0
for i in range(4):
    for j in range(4):
        answer += map[i][j]
    print(answer)
    answer = 0