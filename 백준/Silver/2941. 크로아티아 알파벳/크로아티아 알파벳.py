import sys

word = sys.stdin.readline().strip()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for alpha in croatia:
    word = word.replace(alpha, "a")
    
print(len(word))