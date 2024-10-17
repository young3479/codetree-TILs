#처음에 이차원 배열로 받고 시작
info = [list(input().split()) for _ in range(3)]
count = [0 for _ in range(4)]

for i in info:
    if i[0] == 'Y' and int(i[1]) >= 37:
        count[0] += 1
    elif i[0] == 'N' and int(i[1]) >= 37:
        count[1] += 1
    elif i[0] == 'Y' and int(i[1]) < 37:
        count[2] += 1
    else:
        count[3] += 1

print(*count, end = " ")
if count[0] >= 2:
    print("E")