zero = [1, 0, 1]
one = [0, 1, 1]


def fibo(num):
    l = len(zero)
    if l <= num:
        for i in range(l, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print("%d %d" % (zero[num], one[num]))

n=int(input())
for i in range(n):
    t = int(input())
    fibo(t)