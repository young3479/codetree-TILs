import sys
N = int(input())
A = list(map(int, input().split()))

ans = sys.maxsize

for i in range(N): #5집 각각
    dist = 0
    for j in range(N): #한집씩 이동거리 계산
        dist += abs(i-j) * A[j]

    ans = min(ans, dist)

print(ans)