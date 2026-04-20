import sys

input = sys.stdin.readline

n = int(input())
meet = []
for _ in range(n):
    meet.append(list(map(int, input().split())))

meet.sort(key=lambda x: (x[1],x[0]))

count = 0
last_end_time = 0

for start, end in meet:
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)