import heapq
from collections import Counter, defaultdict
import math

class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def count_frequency(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower().replace(" ", '')
        pair_frequency = Counter(zip(text, text[1:]))
        return pair_frequency

def build_huffman_tree(pair_frequencies):
    heap = [Node(pair, freq) for pair, freq in pair_frequencies.items()]
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
    encoded_text = "".join(codes[pair] for pair in zip(text, text[1:]))
    return encoded_text

def shannon_entropy(frequencies, total_symbols):
    entropy = 0.0
    for freq in frequencies.values():
        probability = freq / total_symbols
        entropy -= probability * (probability and math.log2(probability))
    return entropy

filename = 'text.txt'
text = open(filename, 'r', encoding='utf-8').read().lower().replace(" ", '')

# Считаем частоту пар букв
pair_frequencies = count_frequency(filename)

# Строим дерево Хаффмана
huffman_tree = build_huffman_tree(pair_frequencies)

# Получаем коды Хаффмана
huffman_codes = build_huffman_codes(huffman_tree)

# Выводим закодированный текст
print("Закодированный текст Хаффмана:")
encoded_text = huffman_encode(text, huffman_codes)
print(encoded_text)

# Выводим коды Хаффмана для каждой пары букв
print("\nКоды Хаффмана для каждой пары букв:")
for pair, code in sorted(huffman_codes.items()):
    print(f"Пара '{pair}': {code}")

# Считаем количество бит для кодов Хаффмана
huffman_code_length = len(encoded_text)
print("\nКоличество бит для кодов Хаффмана:", huffman_code_length)
