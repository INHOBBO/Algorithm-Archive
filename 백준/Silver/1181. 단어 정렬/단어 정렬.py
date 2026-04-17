import sys
input = sys.stdin.readline

n = int(input())

dic = []
dic = set(dic)
for _ in range(n):
    dic.add(input().rstrip())
    
dic = list(dic)

dic.sort(key=lambda x:(len(x),x))


for d in dic:
    print(d)