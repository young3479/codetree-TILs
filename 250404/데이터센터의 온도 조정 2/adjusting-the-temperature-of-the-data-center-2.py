import sys
N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

min_a = sys.maxsize
max_b = -sys.maxsize
for a, b in ranges:
    min_a = min(a, min_a)
    max_b = max(b, max_b)

def temperature(i, a, b):
    if i < a:
        t = C
    elif a <= i <= b:
        t = G
    elif i > a:
        t = H
    return t

answer = -sys.maxsize
#작을때 작업량이 더 높을 수 있으니 1부터 시작해야함(min_a가 아닌)
for i in range(1, max_b+1): 
    # i일때 각각의 경우(=N번)를 전부 따져볼 것
    a = 0
    ans = []
    for a, b in ranges:
        a = temperature(i, a, b)
        ans.append(a)
    answer = max(answer, sum(ans))
print(answer)
        

