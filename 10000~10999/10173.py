#https://www.acmicpc.net/problem/10173
#니모를 찾아서

while(1):
    arr=input()
    if arr=="EOI":
        break
    arr=arr.upper()
    if "NEMO" in arr:
        print("Found")
    else:
        print("Missing")