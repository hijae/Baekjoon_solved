#https://www.acmicpc.net/problem/3613
#Java vs C++

s=input()
arr=[]
c=0
if s[len(s)-1]=='_':
    c=1 #마지막 글자가 '_'일때
if s[0]=='_':
    c=2 #첫번째 글자가 '_'일때
if s[0].isupper():
    c=3 #첫번째 글자가 대문자일때
if '__' in s:
    c=4 #'_'가 두개일때
if '_' in s:
    flag=0
    for i in range(len(s)):
        if s[i].isupper():
            c=5 #c++에 대문자가 있을때
        if s[i]=='_':
            flag=1
            continue
        if flag==1:
            arr.append(s[i].upper())
            flag=0
            continue
        else:
            if s[i].isalpha()==False:
                c=6 #알파벳이 아닌 글자가 있을때
            arr.append(s[i])
else:
    for i in range(len(s)):
        if s[i].isalpha()==False:
            c=7 #알파벳이 아닌 글자가 있을때
        if s[i].isupper():
            arr.append('_')
            arr.append(s[i].lower())
        else:
            arr.append(s[i])
if c!=0: #에러 검사후 출력
    print("Error!")
else:
    for i in arr:
        print(i,end='')
    print()