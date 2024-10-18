n = int(input())
nums = list(map(int, input().split()))
desc_nums = sorted(nums, reverse=True)
print(desc_nums[0], desc_nums[1])