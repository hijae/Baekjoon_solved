#https://www.acmicpc.net/problem/10845
#큐
from sys import stdin

n=int(stdin.readline())
q=[]

def push(X): # 정수 X를 큐에 넣는 연산이다.
    q.append(X)
def pop(): # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(q)==0:
        return -1
    else:
        return q.pop(0)
def size(): # 큐에 들어있는 정수의 개수를 출력한다.
    return len(q)
def empty():# 큐가 비어있으면 1, 아니면 0을 출력한다.
    if len(q)==0:
        return 1
    else:
        return 0
def front():# 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(q)==0:
        return -1
    else:
        return q[0]
def back():# 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(q)==0:
        return -1
    else:
        return q[-1]

for i in range(n):
    s=stdin.readline().split()
    if s[0]=="push":
        push(int(s[1]))
    elif s[0]=="pop":
        print(pop())
    elif s[0]=="size":
        print(size())
    elif s[0]=="empty":
        print(empty())
    elif s[0]=="front":
        print(front())
    elif s[0]=="back":
        print(back())

