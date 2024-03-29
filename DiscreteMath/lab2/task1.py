from itertools import combinations

word = "комбинаторика"
word_length = 5

# Генерируем все комбинации из букв слова длиной word_length
combs = combinations(word, word_length)

# Считаем количество комбинаций
num_combinations = sum(1 for _ in combs)

print("Количество 5-буквенных слов из слова 'комбинаторика':", num_combinations)
