#https://www.acmicpc.net/problem/10175
#Dominant Species

n=int(input())
for i in range(n):
    name,arr=input().split()
    name=name.strip()
    spe={'Bobcat':0,'Coyote':0,'Mountain Lion':0,'Wolf':0}
    max=-999
    for j in arr:
        if j=='B':
            spe['Bobcat']+=2
            if max<spe['Bobcat']:
                max=spe['Bobcat']
        if j=='C':
            spe['Coyote']+=1
            if max<spe['Coyote']:
                max=spe['Coyote']
        if j=='M':
            spe['Mountain Lion']+=4
            if max<spe['Mountain Lion']:
                max=spe['Mountain Lion']
        if j=='W':
            spe['Wolf']+=3
            if max<spe['Wolf']:
                max=spe['Wolf']
    psp={}
    flag=0
    for key,num in sorted(spe.items(), key=lambda x: x[1], reverse=True):
        psp[key]=num
        if max==num:
            flag+=1
    if flag==1:
        for key,num in psp.items():
            print("{0}: The {1} is the dominant species".format(name,key))
            break
    else:
        print("{0}: There is no dominant species".format(name))