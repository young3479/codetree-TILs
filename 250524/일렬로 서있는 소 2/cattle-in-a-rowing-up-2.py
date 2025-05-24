N = int(input())
A = list(map(int, input().split()))

# Please write your code here.


count = 0
for i in range(N):
    for j in range(i+1, N):
        for z in range(j+1, N):
            if A[i] <= A[j] and A[j] <= A[z]:
                count += 1

print(count)