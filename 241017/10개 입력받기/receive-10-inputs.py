n = list(map(int, input().split()))
answer = 0
count = 0

for i in n:
    if i != 0:
        answer += i
        count += 1

    else:
        break

print(answer, f"{answer/count:.1f}")