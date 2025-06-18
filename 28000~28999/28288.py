# https://www.acmicpc.net/problem/28288
# Special Event

n = int(input())

days = [0] * 5
for _ in range(n):
	s = input().strip()
	for i in range(5):
		if s[i] == 'Y':
			days[i] += 1
max_days = max(days)
max_count = 0

for day in days:
	if day == max_days:
		max_count += 1

if max_count == 1:
    print(days.index(max_days) + 1)
else:
    result = []
    for i in range(5):
        if days[i] == max_days:
            result.append(str(i + 1))
    print(','.join(result))