n = list(map(int, input().split()))
count = [0 for _ in range(10)]
for i in n:
    if i == 0:
        break
    if i < 10:
        continue
    count[i//10] += 1

for j in range(1, 10):
    print(f"{j} - {count[j]}")