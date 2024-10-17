n, q = map(int, input().split())
nums = list(map(int, input().split()))
question = [list(map(int, input().split())) for _ in range(q)]

for i in range(q):
    if question[i][0] == 1:
        print(nums[question[i][1]-1])
    elif question[i][0] == 2:
        print(nums.index(question[i][1])+1)
    elif question[i][0] == 3:
        print(*nums[question[i][1]-1:question[i][2]])