#https://www.acmicpc.net/problem/1193
#분수찾기

n=int(input()) #입력

end=0
line=0
while n>end: #수열위치 찾기
    line+=1
    end+=line

diff=end-n #찾은 위치와 입력값의 차이
if line%2==0: #짝수일때 차이가 분모
    up=line-diff
    down=diff+1
else: #홀수일때 차이가 분자
    up=diff+1
    down=line-diff

print("{}/{}".format(up,down)) #출력