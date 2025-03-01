N = int(input())
nums = list(map(int,input().split()))

dp = [0] * N

dp[0] = nums[0]


for i in range(1, N):
    dp[i] = max(nums[i], dp[i-1] + nums[i])
    # 연속되지 않으면 초기화되어야함

# print(dp)

print(max(dp))


