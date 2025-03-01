N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

over = [0] * 200

for s, e in info:
    for i in range(s, e):
        over[i] += 1


print(max(over))
