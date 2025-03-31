n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 점을 하나씩 빼고, 그 경우의 직사각형의 넓이를 구해서
# 그 중 작은 넓이를 반환
ans = []
for i in range(n):
    # print(points[i]) #이 좌표를 제외하는 모든 점을 따짐
    final = points[0:i] + points[i+1:n+1]
    x = [p[0] for p in final]
    y = [p[1] for p in final]
    num = (max(x)-min(x)) * (max(y)-min(y))
    ans.append(num)

print(min(ans))