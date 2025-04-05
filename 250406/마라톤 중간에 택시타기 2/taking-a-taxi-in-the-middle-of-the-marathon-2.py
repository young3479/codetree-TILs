import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# N개의 체크 포인트, 중간에 한개 몰래 건너뛰려함(1, N 제외), 이때 최소 거리
# 계산은 abs(절댓값)

# n-2번 반복문을 돌면서 1..n-1 번째 체크 포인트를 건너뛰는 경우를 따져봄
new = []
ans = sys.maxsize
for i in range(1, n-1):
    new = points[:i] + points[i+1:]
    #거리 구하기
    dist = 0
    for j in range(n-2):
        dist += abs(new[j][0] - new[j+1][0]) + abs(new[j][1] - new[j+1][1])
    
    ans = min(dist, ans)

print(ans)
