# https://www.acmicpc.net/problem/5575
# 타임 카드

def time(a,b,c,d,e,f):
    if f>=c:
        s=f-c
    else:
        s=f+60-c
        e-=1
    if e>=b:
        m=e-b
    else:
        m=e+60-b
        d-=1
    h=d-a
    print(h,m,s)

ahs,ams,ass,ahe,ame,ase=map(int,input().split())
time(ahs,ams,ass,ahe,ame,ase)
bhs,bms,bss,bhe,bme,bse=map(int,input().split())
time(bhs,bms,bss,bhe,bme,bse)
chs,cms,css,che,cme,cse=map(int,input().split())
time(chs,cms,css,che,cme,cse)