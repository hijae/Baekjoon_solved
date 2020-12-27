#https://www.acmicpc.net/problem/3009
#네 번째 점

x=[]
y=[]
for i in range(3):
    xt,yt=map(int,input().split())
    x.append(xt)
    y.append(yt)
if x[0]==x[1]:
    ax=x[2]
elif x[0]==x[2]:
    ax=x[1]
else:
    ax=x[0]
if y[0]==y[1]:
    ay=y[2]
elif y[0]==y[2]:
    ay=y[1]
else:
    ay=y[0]
print(ax,ay)