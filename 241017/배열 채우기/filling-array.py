arr = list(map(int, input().split()))
answer = []

for i in arr:
    if i != 0:
        answer.append(i)
    elif i == 0:
        break

print(*answer[::-1])