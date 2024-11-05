s = input()
one = 0
two = 0

for i in range(0, len(s)-1):
    if s[i] == 'e' and s[i+1] == 'e':
        one += 1

    if s[i] == 'e' and s[i+1] == 'b':
        two += 1

print(one, two)