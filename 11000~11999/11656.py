#https://www.acmicpc.net/problem/11656
#접미사 배열

s=input()
arr=[]
for i in s:
    arr.append(s)
    s = s[1:]
arr=sorted(arr)
for i in arr:
    print(i)
