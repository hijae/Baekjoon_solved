# https://www.acmicpc.net/problem/2511
# 카드놀이

a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.reverse()
b.reverse()
a_score=0
b_score=0
for i in range(10):
    if a[i]>b[i]:
        a_score+=3
    elif a[i]<b[i]:
        b_score+=3
    else:
        a_score+=1
        b_score+=1

print(a_score,b_score)
if a_score>b_score:
    print('A')
elif a_score<b_score:
    print('B')
else:
    for i in range(10):
        if a[i]>b[i]:
            print('A')
            break
        elif a[i]<b[i]:
            print('B')
            break
    else:
        print('D')