#https://www.acmicpc.net/problem/4344
#평균은 넘겠지

c=int(input())
for i in range(c):
    score=list(map(int,input().split()))
    sum=0
    for j in range(score[0]):
        sum+=score[j+1]
    cnt=0
    for j in range(score[0]):
        if sum/score[0]<score[j+1]:
            cnt+=1
    print("%.3lf%%"%(cnt/score[0]*100))