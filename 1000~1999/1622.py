#https://www.acmicpc.net/problem/1622
#공통 순열

while(1):
    try:
        arr1=sorted(input())
        arr2=sorted(input())
        if arr1 is None:
            break
        alp1={}
        alp2={}
        for i in range(256):
            alp1[i]=0
        for i in range(256):
            alp2[i]=0
        for i in arr1:
            alp1[ord(i)]+=1
        for i in arr2:
            alp2[ord(i)]+=1
        
        for i in range(256):
            for j in range(min(alp1[i],alp2[i])):
                print(chr(i),end='')
        print()
    except EOFError:
        break