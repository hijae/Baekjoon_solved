#https://www.acmicpc.net/problem/2941
#크로아티아 알파벳

rep=['c=','c-','dz=','d-','lj','nj','s=','z=']
arr=input()

for i in rep:
    arr=arr.replace(i,"*")

print(len(arr))
