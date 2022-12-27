# https://www.acmicpc.net/problem/4358
# 생태학

import sys
from collections import defaultdict

input = sys.stdin.readline

tree = defaultdict(int)
total = 0
while True:
    name = input().rstrip()
    if not name:
        break
    tree[name] += 1
    total += 1

for name in sorted(tree.keys()):
    print(f"{name} {tree[name]/total*100:.4f}")
