# 단어 정렬

# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로

n = int(input())

word_arr = []

word_len_dict = {}

max_len = 0

for i in range(n):
    word = input()
    word_arr.append(word)
    if len(word) >= max_len:
        max_len = len(word)
    if len(word) in word_len_dict:
        if word in word_len_dict[len(word)]:
            continue
        word_len_dict[len(word)].append(word)
    else:
        word_len_dict[len(word)] = [word]


for key, value in word_len_dict.items():
    value.sort()

for i in range(1, max_len+1):
    if i in word_len_dict:
        for j in word_len_dict[i]:
            print(j)

