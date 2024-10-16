nums = list(map(int, input().split()))
answer = []
count = 0

for i in nums:
    if i < 250:
        answer.append(i)
        count += 1
    else:
        break
print(sum(answer), sum(answer)/count)