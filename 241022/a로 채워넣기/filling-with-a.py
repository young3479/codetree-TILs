a = list(input())

a[1] = 'a'
a[-2] = 'a'
print(*a, sep="")