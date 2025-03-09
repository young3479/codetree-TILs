N, T = map(int, input().split()) #행, 초
R, C, D = input().split() #초기행, 초기열, 방향

mapper = {} #딕셔너리
mapper['U'] = 0
mapper['L'] = 1
mapper['D'] = 2
mapper['R'] = 3

# 1. 0,1,2,3 방향을 정한다. (어디가 0인지, 시계&반시계)
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
x, y = int(R), int(C)
direct = mapper[D]

def in_range(x, y):
    return 1 <= x and x < N+1 and 1 <= y and y < N+1

for i in range(T): #T초 동안 움직임
    # 바로 가는게 아니라 nx에 잠시 담아서 아래에서 갈 수 있는 지 체크
    nx = x + dx[direct] 
    ny = y + dy[direct]
    
    # 단 갈 수 있으면 직진하고
    if in_range(nx, ny):
        x = nx
        y = ny
    else: # 못가면 회전 (반대로)
        direct = (direct + 2) % 4

print(x, y)