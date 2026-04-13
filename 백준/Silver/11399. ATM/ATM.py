import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

total = 0
time = 0
for t in arr:
	time += t
	total += time
print(total, end=" ")