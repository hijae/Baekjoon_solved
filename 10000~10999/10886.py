# https://www.acmicpc.net/problem/10886
# 0 = not cute / 1 = cute

n=int(input())
cute=0
ncute=0
for i in range(n):
    t=input()
    if t=='1':
        cute+=1 # 귀여우면
    else:
        ncute+=1 # 안귀여우면
if cute>ncute: # 귀여우면이 많으면
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")