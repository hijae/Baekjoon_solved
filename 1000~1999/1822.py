#https://www.acmicpc.net/problem/1822
#차집합

na,nb=map(int,input().split())  #각 집합의 갯수 입력
a=list(map(int,input().split()))  #집합A 입력
b=list(map(int,input().split()))  #집합B 입력

amb=list(set(a)-set(b))  #하나의 집합에 속하는 모든 원소의 값은 다르다는 조건에 따라 가능
print(len(amb))  #차집합 연산 후 개수 출력
amb=sorted(amb)  #순서대로 정렬
for i in amb:
    print(i,end=" ")  #출력