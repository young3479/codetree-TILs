info = list(input())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0 # 초기 좌표 위치
direct = 0 # 북쪽 바라보고 시작
time = 0

for i in info:
    if i == 'F':
        x = x + dx[direct]
        y = y + dy[direct]
        time += 1

    elif i == 'L':
        direct = (direct + 3) % 4 # 명령 L일 때
        time += 1

    elif i == 'R':
        direct = (direct + 1) % 4 # 명령 R일 때 
        time += 1
    
    else:
        print("잘못된 입력입니다.")

    if x == 0 and y == 0:
        break

if x != 0 and y != 0:
    time = -1
    
print(time)

