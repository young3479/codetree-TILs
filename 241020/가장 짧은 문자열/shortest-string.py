a =len(input())
b =len(input())
c =len(input())

max_st = max(a, b, c)
min_st = min(a, b, c)
answer = max_st - min_st
print(answer)