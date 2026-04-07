n = int(input())

word_count = n

for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                word_count -= 1
                break

print(word_count)