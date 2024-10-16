#학생 수 
#각 학생별 4과목 점수

students = int(input())
count = 0

for i in range(students):
    scores = list(map(int, input().split()))
    aver = sum(scores)/4
    if aver >= 60:
        print("pass")
        count += 1
    else: 
        print("fail")
print(count)