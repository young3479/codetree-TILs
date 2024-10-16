n = int(input())
nums = list(map(int, input().split()))
count = [0 for _ in range(9)]

for i in nums:
    count[i-1] += 1

print(*count, sep ="\n")