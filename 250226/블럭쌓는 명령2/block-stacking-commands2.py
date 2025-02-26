# 각각의 방을 배열로 만들어서, 방마다 청소를 했는지 아닌지 표시
# 처음에 다 0을 채워놓고 시작해서, 청소한건 1로 변경

N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(K)]

#0이 N개 있는 배열 만들기
block = [ 0 for i in range(N+1)]

for s, e in info:
    for j in range(s, e+1):
        block[j] += 1

print(max(block))