#https://www.acmicpc.net/problem/5622
#다이얼

text=input()
cnt=0
for i in range(len(text)):
    if text[i]<='C':
        cnt+=3
    elif text[i]<='F':
        cnt+=4
    elif text[i]<='I':
        cnt+=5
    elif text[i]<='L':
        cnt+=6
    elif text[i]<='O':
        cnt+=7
    elif text[i]<='S':
        cnt+=8
    elif text[i]<='V':
        cnt+=9
    else:
        cnt+=10
print(cnt)