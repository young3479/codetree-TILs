n = int(input())
start = 'A'
count = 0

for i in range(n):
    for j in range(i+1):
        print(chr(ord(start)+count), end="")
        if count <= 26:
            count+=1
        else:
            count-=27
    print()