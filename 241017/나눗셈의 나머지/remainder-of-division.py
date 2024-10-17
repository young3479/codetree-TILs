a, b = map(int, input().split())
count = [0 for _ in range(10)] #나머지는 1~9임
answer = 0

while a > 1: #a가 1보다 클동안 수행할 작업
    a = a//b
    count[a%b] += 1

for i in count:
    answer = answer + i**2
    
print(answer)