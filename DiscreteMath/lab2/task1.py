from itertools import combinations

word = "комбинаторика"
word_length = 5

combs = combinations(word, word_length)
for item in combs:
    print(item)

combs = combinations(word, word_length)
num_combinations = sum(1 for _ in combs)
print("Количество 5-буквенных слов из слова 'комбинаторика':", num_combinations)

