n = int(input()) #관찰한 횟수, 몇번 비둘기 어는 위치
positions = [list(map(int, input().split())) for _ in range(n)]
moves = [[] for _ in range(11)]
count = 0

for pigeon, pos in positions:
    moves[pigeon].append(pos)

for j in moves:
    for x in range(len(j)-1):
        if j[x] != j[x+1]:
            count += 1
print(count)