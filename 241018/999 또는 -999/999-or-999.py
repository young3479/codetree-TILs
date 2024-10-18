nums = list(map(int, input().split()))
# 초기값을 리스트의 첫 번째 값으로 설정
max_num = nums[0]
min_num = nums[0]

for i in nums:
    if i == 999 or i == -999:
        break
    elif i >= max_num:
        max_num = i
    elif i <= min_num:
        min_num = i

print(max_num, min_num)