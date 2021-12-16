#https://www.acmicpc.net/problem/10828
#스택

import sys
stack=[]

n=int(sys.stdin.readline())

for i in range(n):
    t=sys.stdin.readline().split() #속도를 위해 input대신 사용
    if t[0]=="push":
        stack.append(int(t[1]))
    if t[0]=="pop":
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    if t[0]=="size":
        print(len(stack))
    if t[0]=="empty":
        if stack:
            print(0)
        else:
            print(1)
    if t[0]=="top":
        if stack:
            print(stack[-1])
        else:
            print(-1)