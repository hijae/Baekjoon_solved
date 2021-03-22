#https://www.acmicpc.net/problem/5656
#비교 연산자

i=0
while(1):
    arr=input()
    i+=1
    if arr[2]=='E':
        break
    else:
        print("Case {}: ".format(i)+str(eval(arr)).lower())