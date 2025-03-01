N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(K)]

block = [0] * (N + 1)

for s, e in info:
    for i in range(s, e+1):
        block[i] += 1
    
print(max(block))
