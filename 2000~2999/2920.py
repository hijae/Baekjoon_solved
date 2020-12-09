#https://www.acmicpc.net/problem/2920
#음계

up=[1,2,3,4,5,6,7,8]
down=[8,7,6,5,4,3,2,1]
arr=list(map(int,input().split()))

if arr==up:
    print("ascending")
elif arr==down:
    print("descending")
else:
    print("mixed")