scores = list(map(int, input().split()))
count = [0 for _ in range(11)]

for i in scores:
    if i == 0:
        break
    if i < 10:
        continue
    count[i//10] += 1
    
for j in range(10, 0, -1):
    print(f"{j*10} - {count[j]}")