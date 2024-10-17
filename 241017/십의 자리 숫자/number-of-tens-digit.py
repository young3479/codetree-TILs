n = list(map(int, input().split()))
count = [0 for _ in range(9)]
for i in n:
    if i != 0:
        if len(str(i)) != 1:
            i = int(i//10)
            count[i-1] += 1
    else:
        break

for j in range(1, 10):
    print(f"{j} - {count[j-1]}")