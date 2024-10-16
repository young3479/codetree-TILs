n = int(input())
arrs = list(map(int, input().split()))
new = [arr**2 for arr in arrs]
print(*new)