a, b = input().split()
a, b = ord(a), ord(b)
if b>a:
    a, b = b, a
    
print(a+b, a-b)