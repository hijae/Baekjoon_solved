#https://www.acmicpc.net/problem/2942
#퍼거슨과 사과

r,g=map(int,input().split())

a,b=r,g
if(a>b) : a,b = b,a

while(b!=0):
    a=a%b
    a,b=b,a
i=1
while i*i<=a:
    if a%i==0:
        print(i,r//i,g//i)
        if a//i!=i:
            print(a//i,r//(a//i),g//(a//i))
    i+=1