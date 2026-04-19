import sys

input = sys.stdin.readline

n = int(input())
member = []

for i in range(n):
    member.append(input().split()) # member 리스트

member.sort(key=lambda x: int(x[0]))

for m in member:
    print(m[0], m[1])