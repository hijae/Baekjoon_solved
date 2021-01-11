#https://www.acmicpc.net/problem/10179
#쿠폰

n=int(input())
for i in range(n):
    t=float(input())
    print('$%.2f'%(t*0.8))