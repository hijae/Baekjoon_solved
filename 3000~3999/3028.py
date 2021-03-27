#https://www.acmicpc.net/problem/3028
#창영마을

cup=[1,0,0]
arr=list(input())
for i in arr:
    if i=='A':
        cup[0],cup[1]=cup[1],cup[0]
    if i=='B':
        cup[1],cup[2]=cup[2],cup[1]
    if i=='C':
        cup[0],cup[2]=cup[2],cup[0]
for i,n in enumerate(cup):
    if n==1:
        print(i+1)