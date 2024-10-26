n = int(input()) #관찰한 횟수, 몇번 비둘기 어는 위치
positions = [list(map(int, input().split())) for _ in range(n)]
moves = [[] for _ in range(11)]
count = 0

for i in positions:
    moves[i[0]].append(i[1])

for j in moves:
    if len(j) >= 2:
        # 앞뒤가 똑같으면 안됨. 즉 1->0 0->1로 상태가 바뀔때마다 체크
        # 으아아아아악 어케 체크할까 너무 괴롭다.....
        for x in range(len(j)-1):
            if j[x] != j[x+1]:
                count += 1
print(count)