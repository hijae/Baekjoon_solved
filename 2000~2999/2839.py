#https://www.acmicpc.net/problem/2839
#설탕 배달

a=int(input())
if a%5==0:
    n=a//5
elif a%5==1 and a>=6:
    n=2+((a-6)//5)
elif a%5==2 and a>=12:
    n=4+((a-12)//5)
elif a%5==3 and a>=3:
    n=1+((a-3)//5)
elif a%5==4 and a>=9:
    n=3+((a-9)//5)
else:
    n=-1
print(n)