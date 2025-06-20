# https://www.acmicpc.net/problem/17293
# 맥주 99병

N = int(input())

for i in range(N, 0, -1):
	if i == 1:
		print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
		print("Take one down and pass it around, no more bottles of beer on the wall.\n")
	else:
		print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
		if i - 1 == 1:
			print(f"Take one down and pass it around, {i-1} bottle of beer on the wall.\n")
		else:
			print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.\n")
print("No more bottles of beer on the wall, no more bottles of beer.")
if N == 1:
	print(f"Go to the store and buy some more, {N} bottle of beer on the wall.")
elif N > 1:
	print(f"Go to the store and buy some more, {N} bottles of beer on the wall.")
elif N == 0:
	print("Go to the store and buy some more, no more bottles of beer on the wall.")