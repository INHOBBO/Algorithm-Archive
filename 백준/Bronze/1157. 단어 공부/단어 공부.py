from collections import Counter

word = input().upper()
word_counter = Counter(word)

max_value = max(word_counter.values())

answer = []

for key in list(word_counter.keys()):
	if word_counter[key] == max_value:
		answer.append(key)
	
if len(answer) > 1:
	print('?')
else:
	print(answer[0])