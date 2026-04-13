import sys

n = int(sys.stdin.readline())

word_list = []
for _ in range(n):
	word_list.append(sys.stdin.readline().strip())

word_list_set = list(set(word_list))

word_list_sorted = sorted(word_list_set, key=lambda x: (len(x), x))

for word in word_list_sorted:
	print(word)
