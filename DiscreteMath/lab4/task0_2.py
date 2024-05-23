from collections import Counter
import heapq
import math

def count_character_frequency(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower().replace(" ", '')
        character_frequency = Counter(text)
        pair_frequency = Counter(zip(text, text[1:]))  # Считаем частоту пар букв
        return character_frequency, pair_frequency

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
        
    return heap[0]

def build_huffman_codes(node, prefix="", codes={}):
    if node is not None:
        if node.value is not None:
            codes[node.value] = prefix
        build_huffman_codes(node.left, prefix + "0", codes)
        build_huffman_codes(node.right, prefix + "1", codes)
    return codes

def huffman_encode(text, codes):
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text

def huffman_decode(encoded_text, root):
    decoded_text = ""
    current = root
    for bit in encoded_text:
        if bit == "0":
            current = current.left
        else:
            current = current.right
        if current.value is not None:
            decoded_text += current.value
            current = root
    return decoded_text

def shannon_entropy(frequencies, total_symbols):
    entropy = 0.0
    for freq in frequencies.values():
        probability = freq / total_symbols
        entropy -= probability * (probability and math.log2(probability))
    return entropy

def encode_huffman_tree(root):
    if root is None:
        return ""

    if root.value is not None:
        return "1" + bin(ord(root.value))[2:].zfill(8)  # 1 + 8-bit ASCII код символа

    return "0" + encode_huffman_tree(root.left) + encode_huffman_tree(root.right)

class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

filename = 'text.txt'
character_frequency, pair_frequency = count_character_frequency(filename)

print("Частота каждого символа в тексте:")
for char, freq in character_frequency.items():
    print(f"Символ '{char}': {freq}")

print("\nЧастота пар букв в тексте:")
for pair, freq in pair_frequency.items():
    print(f"Пара '{pair}': {freq}")

filename = 'text.txt'
with open(filename, 'r', encoding='utf-8') as file:
    text = file.read().lower().replace(" ", '')
    character_frequency = Counter(text)

huffman_tree = build_huffman_tree(character_frequency)
huffman_codes = build_huffman_codes(huffman_tree)
encoded_text = huffman_encode(text, huffman_codes)

# Вывод закодированного текста Хаффмана
print("\nЗакодированный текст Хаффмана:")
print(encoded_text)

# Вывод кодов Хаффмана для каждого символа
print("\nКоды Хаффмана для каждого символа:")
for char, code in sorted(huffman_codes.items()):
    print(f"Символ '{char}': {code}")

# Считаем количество бит для равномерных кодов (5-ти битовые)
uniform_code_length = 5 * len(text)

# Считаем количество бит для кодов Хаффмана
huffman_code_length = len(encoded_text)

# Считаем количество информации по формуле Шеннона
total_symbols = sum(character_frequency.values())
shannon_information = shannon_entropy(character_frequency, total_symbols) * total_symbols

print("\nКоличество бит для равномерных кодов (5-ти битовые):", uniform_code_length)
print("Количество бит для кодов Хаффмана:", huffman_code_length)
print("Количество информации по формуле Шеннона:", shannon_information)

# Закодированное дерево Хаффмана
encoded_tree = encode_huffman_tree(huffman_tree)
print("\nЗакодированное дерево Хаффмана:")
print(encoded_tree)
print("Длина закодированного дерева Хаффмана в битах:", len(encoded_tree))
