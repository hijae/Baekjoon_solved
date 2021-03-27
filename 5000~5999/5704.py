#https://www.acmicpc.net/problem/5704
#팬그램

from string import ascii_lowercase
alp={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','n','o','p','q','r','s','t','u','v','w','x','y','z'}
while True:
    arr=set(input().replace(" ",''))
    if arr=={'*'}:
        break
    if alp.issubset(arr):
        print("Y")
    else:
        print("N")