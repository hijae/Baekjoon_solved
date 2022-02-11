#https://www.acmicpc.net/problem/1026
#보물

#a,b를 각각 큰 순서, 작은 순서대로 배열해서 곱한 값을 더하면 답이 나온다.
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort(reverse=True) # 정렬
b.sort()
sum=0
for i in range(n):
    sum+=a[i]*b[i]
print(sum)