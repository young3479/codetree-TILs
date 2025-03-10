N = int(input())
info = [list(input().split()) for _ in range(N)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

mapper = {}
mapper['N'] = 0
mapper['E'] = 1
mapper['S'] = 2
mapper['W'] = 3

x, y = 0, 0
time = 0
exit_flag = False

for i in info:
    #만일 0,0이면 break
    direct, distance = mapper[i[0]], int(i[1])

    for j in range(distance):
        x = x + dx[direct]
        y = y + dy[direct]
        time += 1
        # print("x&y", x, y)
        # print("time", time)
        if x == 0 and y == 0:
            exit_flag = True
            break
    if exit_flag:
        break

    
print(time)

    


# while(x == 0 and y == 0):
#     #만일 N을 다 수행 했는데도 0,0 못하면 break
