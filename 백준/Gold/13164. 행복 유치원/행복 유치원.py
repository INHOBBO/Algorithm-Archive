import sys

input = sys.stdin.readline

n, k = map(int, input().split())

kids = list(map(int, input().split()))
diff = [] #인접한 원생과의 키차이를 저장
for i in range(0,n-1):
    diff.append(kids[i+1]-kids[i]) #i번째 원생과 i+1번째 원생 사이의 키차이
    
diff.sort() #키차이를 오름차순으로 정렬
sum = 0
for i in range(n-k): #n-k개의 키차이를 더함
    sum += diff[i]
    
print(sum)