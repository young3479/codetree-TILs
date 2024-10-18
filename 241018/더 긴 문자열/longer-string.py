n, m = input().split()

if len(n) > len(m):
    print(n, len(n))
elif len(n) < len(m):
    print(m, len(m))
else:
    print("same")