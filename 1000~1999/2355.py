#https://www.acmicpc.net/problem/2355
#시그마

a, b = input().split()
miny=min(int(a),int(b))
maxy=max(int(a),int(b))
n=maxy-miny
s = (n * (n + 1)) // 2
print(s + (miny * (n + 1)))