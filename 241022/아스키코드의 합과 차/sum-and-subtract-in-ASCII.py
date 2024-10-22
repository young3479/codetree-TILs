a, b = input().split()
a, b = int(ord(a)), int(ord(b))
if b>a:
    a, b = b, a
    
print(a+b, a-b)