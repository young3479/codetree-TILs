a = input()

#일반적으로 하면 z했을때 { 나옴, 따라서 z는 따로 처리
if a == 'z':
    print('a')
else:
    print(chr(ord(a)+1))