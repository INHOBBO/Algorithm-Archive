import sys

input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))

graph_set = sorted(list(set(graph)))

dic = {} # 빈 사물함 만들기
for i, val in enumerate(graph_set):
    dic[val] = i


for num in graph:
    print(dic[num], end=' ')