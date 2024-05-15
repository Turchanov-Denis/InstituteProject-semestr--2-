import math


def lzw_encode(text):
    dictionary_size = 256
    dictionary = {chr(i): i for i in range(dictionary_size)}
    encoded_text = []
    current_sequence = ""

    for char in text:
        new_sequence = current_sequence + char
        if new_sequence in dictionary:
            current_sequence = new_sequence
        else:
            encoded_text.append(dictionary[current_sequence])
            dictionary[new_sequence] = dictionary_size
            dictionary_size += 1
            current_sequence = char

    if current_sequence:
        encoded_text.append(dictionary[current_sequence])

    return encoded_text, dictionary


def lzw_decode(encoded_text, dictionary):
    decoded_text = ""
    dictionary_size = 256
    inverse_dictionary = {v: k for k, v in dictionary.items()}
    current_sequence = chr(encoded_text.pop(0))
    decoded_text += current_sequence

    for code in encoded_text:
        if code in inverse_dictionary:
            entry = inverse_dictionary[code]
        elif code == dictionary_size:
            entry = current_sequence + current_sequence[0]
        else:
            raise ValueError("Bad compressed code")

        decoded_text += entry
        dictionary[current_sequence + entry[0]] = dictionary_size
        dictionary_size += 1
        current_sequence = entry

    return decoded_text


# Считываем текст из файла
filename = 'text.txt'
with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

# Кодируем текст с помощью LZW
encoded_text, dictionary = lzw_encode(text)

# Декодируем закодированный текст
decoded_text = lzw_decode(encoded_text, dictionary)

# Выводим закодированный текст и сравниваем с оригиналом
print("Закодированный текст LZW:")
print(encoded_text)
print("\nДекодированный текст LZW:")
print(decoded_text)

# Сравниваем длины закодированного текста и оригинала
print("\nДлина исходного текста:", len(text))
print("Длина закодированного текста:", len(encoded_text))
# Определяем размер словаря
dictionary_size = len(set(encoded_text))

# Вычисляем количество бит
bit_count = len(encoded_text) * math.log2(dictionary_size)

print("Количество бит для закодированного текста:", bit_count)
