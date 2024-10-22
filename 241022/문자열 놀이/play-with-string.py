s, q = input().split()
s = list(s)
q = int(q)
ques = [list(input().split()) for _ in range(q)]
temp = 0

for i in range(q):
    if int(ques[i][0]) == 1:
        temp = s[int(ques[i][1])-1]
        s[int(ques[i][1])-1] = s[int(ques[i][2])-1]
        s[int(ques[i][2])-1] = temp
        print(*s, sep="")

    elif int(ques[i][0]) == 2:
        for j in range(len(s)):
            if s[j] == ques[i][1]:
                s[j] = ques[i][2]
        print(*s, sep="")