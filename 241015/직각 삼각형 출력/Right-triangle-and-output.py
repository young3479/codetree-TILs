n = int(input())
count = 1
for i in range(n):
    for j in range(i+count):
        print("*", end="")   
    print()
    count+=1