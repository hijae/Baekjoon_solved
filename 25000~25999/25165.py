# https://www.acmicpc.net/problem/25165
# 영리한 아리의 포탈 타기

n,m=map(int,input().split())
a,d=map(int,input().split())
r,c=map(int,input().split())

if n-1>=r:
    print("NO...")
    exit(0)
if (n+d)%2==0:
    print("NO...")
    exit(0)
print("YES!")