A, B, C, D = map(int, input().split())

#2시 5분 ~ 4시 1분

# 일반 구현
# answer = (60 * C + D) - (60 * A + B)
# print(answer)

# 시뮬레이션
cnt = 0
while True:
    if A == C and B == D:
        break

    B += 1
    cnt += 1

    if B == 60:
        A += 1
        B = 0

print(cnt)