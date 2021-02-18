#https://www.acmicpc.net/problem/1085
#직사각형에서 탈출

x,y,w,h=map(int,input().split())
if x>w-x:
    xmin=w-x
else:
    xmin=x
if y>h-y:
    ymin=h-y
else:
    ymin=y
if xmin>ymin:
    print(ymin)
else:
    print(xmin)