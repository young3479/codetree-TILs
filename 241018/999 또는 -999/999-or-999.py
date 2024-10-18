nums = list(map(int, input().split()))
max_num = -999
min_num = 999
for i in nums:
    if i == 999 or i == -999:
        break
    elif i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i

print(max_num, min_num)