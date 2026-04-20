import sys

input = sys.stdin.readline

score = [] 

for i in range(5):
    score.append(int(input()))
             
total_score = 0

for i in range(len(score)):
    total_score += score[i]

print(total_score//len(score))

score.sort()
print(score[len(score)//2])