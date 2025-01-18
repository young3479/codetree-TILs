money = int(input())

if money >= 3000:
    print("book")
elif money >= 1000 and money < 3000:
    print("mask")
elif money >= 500 and money < 1000:
    print("pen")
else:
    print("no")