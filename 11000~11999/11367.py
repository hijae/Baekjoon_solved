#https://www.acmicpc.net/problem/11367
#Report Card Time

n=int(input())
for i in range(n):
    name,t=input().split()
    t=int(t)
    print(name,end=' ')
    if t>=97:
        print("A+")
    elif t>=90:
        print("A")
    elif t>=87:
        print("B+")
    elif t>=80:
        print("B")
    elif t>=77:
        print("C+")
    elif t>=70:
        print("C")
    elif t>=67:
        print("D+")
    elif t>=60:
        print("D")
    else:
        print("F")