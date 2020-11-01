#https://www.acmicpc.net/problem/2753
#윤년

n=int(input())
print(((n%4==0 and n%100 !=0) or n%400==0)*1)