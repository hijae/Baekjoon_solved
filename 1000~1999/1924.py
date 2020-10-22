arr=[31,28,31,30,31,30,31,31,30,31,30,31]
n=0
x,y = input().split()
x=int(x)
y=int(y)

for i in range(0,x-1):
    n+=arr[i]
n+=y
if n%7==1:
    print("MON")
if n%7==2:
    print("TUE")
if n%7==3:
    print("WED")
if n%7==4:
    print("THU")
if n%7==5:
    print("FRI")
if n%7==6:
    print("SAT")
if n%7==0:
    print("SUN")