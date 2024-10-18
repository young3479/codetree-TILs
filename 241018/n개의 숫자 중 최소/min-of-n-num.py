n = int(input())
nums = list(map(int, input().split()))
min_num = min(nums)
count = 0

for i in nums:
    if i == min_num:
        count += 1

print(min_num, count)