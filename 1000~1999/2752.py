#https://www.acmicpc.net/problem/2752
#세수정렬

a=list(map(int,input().split()))
a.sort()
for i in a:
    print(i,end=' ')