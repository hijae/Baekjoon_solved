#https://www.acmicpc.net/problem/1316
#그룹 단어 체커

cnt = 0
n=int(input())
for i in range(n):
    word = input()
    if list(word) == sorted(word, key=word.find):
        cnt=cnt+1

print(cnt)
