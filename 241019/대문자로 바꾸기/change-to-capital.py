map = [list(input().split()) for _ in range(5)]

for i in range(5):
    for j in range(3):
        print(map[i][j].upper(), end=" ")
    print()