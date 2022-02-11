#https://www.acmicpc.net/problem/15727
#조별과제를 하려는데 조장이 사라졌다

n=int(input())
if n%5==0: #5의배수 거리에 있을때
    print(n//5)
else: #5의배수 거리보다 조금 더 갈때
    print(n//5+1)