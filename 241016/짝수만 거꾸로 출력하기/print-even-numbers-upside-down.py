n = int(input())
nums = list(map(int, input().split()))
answer = []

for i in nums:
    if i % 2 == 0:
        answer.append(i)    
    else:
        continue

print(*answer[::-1])