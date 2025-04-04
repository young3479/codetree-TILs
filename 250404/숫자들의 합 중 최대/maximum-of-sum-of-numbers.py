import sys
X, Y = map(int, input().split())

ans = -sys.maxsize
# X이상 Y이하 수 중에서 각 자리 숫자 합 구하기: 차례대로
# 현재 계산 값과 ans의 값 비교해서 더 큰 숫자를 ans에 저장

for i in range(X, Y+1):
    nums = []
    #방법 1. //, % 사용해서 한 자리 수 씩 끊어서 더하기
    #만일 i가 세자리수 이상이면 계속 돌아야함
    #9999이면 최대 3번 i//10 | 10000이면 4번
    # total = 0
    while(i != 0):
        nums.append(i%10)
        i = i//10
    ans = max(ans, sum(nums))

print(ans)
        
    