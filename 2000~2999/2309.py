#https://www.acmicpc.net/problem/2309
#일곱 난쟁이

arr=[]
for i in range(9):
    arr.append(int(input()))
arr.sort()
flag=0
for i in range(9):
    if flag==1:
        break
    for j in range(9):
        if flag==1:
            break
        sum=0
        for k in range(9):
            if k==i or k==j or i==j:
                pass
            else:
                sum+=arr[k]
        if sum==100:
            flag=1
            for k in range(9):
                if k==i or k==j:
                    pass
                else:
                    print(arr[k])