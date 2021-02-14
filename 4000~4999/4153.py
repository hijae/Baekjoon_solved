#https://www.acmicpc.net/problem/4153
#직각삼각형

while(True):
    arr=map(int,input().split())
    arr=sorted(arr)
    if arr[0]==0 or arr[1]==0 or arr[2]==0:
        break
    if arr[0]**2+arr[1]**2==arr[2]**2:
        print("right")
    else:
        print("wrong")