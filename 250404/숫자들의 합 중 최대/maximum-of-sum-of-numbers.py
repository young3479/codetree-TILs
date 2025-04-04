import sys
X, Y = map(int, input().split())

# ans = -sys.maxsize
# X이상 Y이하 수 중에서 각 자리 숫자 합 구하기: 차례대로
# 현재 계산 값과 ans의 값 비교해서 더 큰 숫자를 ans에 저장
ans = []

for i in range(X, Y+1):
    #방법 1. //, % 사용해서 한 자리 수 씩 끊어서 더하기
    #방법 2. 숫자를 하나씩 끊어서 list에 담고 sum()

    #만일 i가 세자리수 이상이면 계속 돌아야함
    while(i>9):
        sec = i//10
        fir = i%10
        i = i//10
        total = sec+fir
        # print(sec, fir, i)

    ans.append(total)

print(max(ans))
        
    #9999이면 최대 3번 i//10 | 10000이면 4번