n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))


#123
#651

#2번째 마지막을 temp, 1번째 마지막을 temp


for _ in range(t):
    # 1번째 마지막을 temp
    temp = u[n-1]

    # 1번째 값 이동
    for i in range(n-1, 0, -1):
        u[i] = u[i-1]

    # 2 마지막을 1번째의 1번으로 
    u[0] = d[n-1]

    # 2번째 값 이동
    for j in range(n-1, 0, -1):
        d[j] = d[j-1]

    d[0] = temp 


print(*u)
print(*d)

