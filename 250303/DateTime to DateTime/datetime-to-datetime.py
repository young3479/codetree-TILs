# 11월 11일 11시 11분에서 
# 11월 A일 B시 C분까지 몇분이 걸리는 지
# 우선 분이 60보다 크면 시간 하나 증가
# 시간이 24보다 크면 일이 하나 증가 
# 시간이 11, 11, 11 에서 시작하여 A, B, C와 동일할 때까지 진행

A, B, C = map(int, input().split())

# 단 11,11,11 보다 앞서면 -1 출력

if A < 11:
    print(-1)
elif A == 11 and B < 11:
    print(-1)
elif A == 11 and B == 11 and C < 11:
    print(-1)

day, hour, minute = 11, 11, 11
cnt = 0

while(True):
    if day == A and hour == B and minute == C:
        break
    
    if minute == 60:
        hour += 1
        minute = 0

    if hour == 24:
        day += 1
        hour = 0

    minute += 1
    cnt += 1

print(cnt)
