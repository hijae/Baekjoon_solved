#https://www.acmicpc.net/problem/10156
#과자

k,n,m=map(int,input().split())
print(k*n-m if k*n-m>0 else 0)