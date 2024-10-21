n = int(input())
nums = input().split()
concat_str = ''.join(nums)

for i in range(0, len(concat_str), 5):
    print(concat_str[i:i+5])