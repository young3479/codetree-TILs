n = int(input())
words = [
    input()
    for _ in range(n)
]

count = 0
a = 0

for i in words:
    count += len(i)
    if i[0] == 'a':
        a += 1

print(count, a)