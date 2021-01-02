#https://www.acmicpc.net/problem/5543
#상근날드

burgermin,drinkmin=9999,9999
for i in range(3):
    t=int(input())
    if burgermin>t:
        burgermin=t
for i in range(2):
    t=int(input())
    if drinkmin>t:
        drinkmin=t
print(burgermin+drinkmin-50)