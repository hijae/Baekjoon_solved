n=int(input())
cnt=0
for i in range(1,n+1):
    if i>=100:
        flag=i//100-(i//10)%10
        if flag==(i//10)%10-i%10:
            cnt+=1
    else:
        cnt+=1
print(cnt)