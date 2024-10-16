nums = list(map(int, input().split()))
count = [0 for _ in range(6)]
dice = 0

for i in nums:
    count[i-1] += 1

for j in count:
    dice += 1
    print(f"{dice} - {j}")