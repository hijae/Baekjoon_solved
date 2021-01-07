#https://www.acmicpc.net/problem/10039
#평균 점수

sum=0
for i in range(5):
    t=int(input())
    if t>=40:
        sum+=t
    else:
        sum+=40
print(sum//5)