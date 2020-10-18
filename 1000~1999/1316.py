cnt = 0
n=int(input())
for i in range(n):
    word = input()
    if list(word) == sorted(word, key=word.find):
        cnt=cnt+1

print(cnt)
