words = ["apple", "banana", "grape", "blueberry", "orange"]
a = input()
count = 0

for i in range(5):
    if words[i][2] == a:
        print(words[i])
        count += 1
    elif words[i][3] == a:
        print(words[i])
        count += 1
    else:
        continue

print(count)