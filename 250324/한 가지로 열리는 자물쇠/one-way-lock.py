N = int(input())
a, b, c = map(int, input().split())

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for z in range(1, N+1):
            if a-2 <= i <= a+2 or b-2 <= j <= b+2 or c-2 <= z <= c+2:
                cnt += 1

print(cnt)


