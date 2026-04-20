import sys

input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

graph.sort(key=lambda x:(x[1],x[0]))

for x, y in graph:
    print(x, y)

# 좌표를 y좌표가 증가하는 순으로,
# y좌표가 같으면 x좌표가 증가하는 순서