arr=input()
for i in arr:
    if i>='A' and i<='Z':
        if chr(ord(i)+13)>'Z':
            print(chr(ord(i)-13),end='')
        else:
            print(chr(ord(i)+13),end='')
    elif i>='a' and i<='z':
        if chr(ord(i)+13)>'z':
            print(chr(ord(i)-13),end='')
        else:
            print(chr(ord(i)+13),end='')
    else:
        print(i,end='')
print()