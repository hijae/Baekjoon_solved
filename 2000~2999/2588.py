#https://www.acmicpc.net/problem/2588
#곱셈

i=int(input())
j=int(input())
n=j%10*i
print(j%10*i)
j//=10
n=n+(j%10*i)*10
print(j%10*i)
j//=10
n=n+(j%10*i)*100
print(j%10*i)
print(n)