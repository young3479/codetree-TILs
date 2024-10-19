n = int(input())
nums = list(map(int, input().split()))
two_count = 0
for i in range(n):
    if two_count == 3:
        print(nums.index(nums[i]))
        # print("카운트 3일때", i)
        break
    if nums[i] == 2:
        two_count += 1
        # print("2일때", i)
        continue
    else:
        continue