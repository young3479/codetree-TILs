n = int(input())
start = 'A'
count = -1

for i in range(n):
    for j in range(i+1):
        if count <= 24:
            count+=1
        else:
            count-=25
        print(chr(ord(start)+count), end="")
    print()