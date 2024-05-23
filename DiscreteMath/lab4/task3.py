import statistics
def initialize_dictionary():
    # Инициализация словаря с односимвольными строками
    dictionary = {chr(i): i for i in range(256)}
    return dictionary, 256

def lzw_compress(input_string):
    dictionary, dict_size = initialize_dictionary()
    current_string = ""
    compressed_data = []
    
    for symbol in input_string:
        string_plus_symbol = current_string + symbol
        if string_plus_symbol in dictionary:
            current_string = string_plus_symbol
        else:
            compressed_data.append(dictionary[current_string])
            dictionary[string_plus_symbol] = dict_size
            dict_size += 1
            current_string = symbol
    
    if current_string:
        compressed_data.append(dictionary[current_string])
    
    return compressed_data

def calculate_encoded_bits(compressed_data):
    print(compressed_data)
    max_code = max(compressed_data)
    bits_per_code = max_code.bit_length()
    total_bits = len(compressed_data) * bits_per_code 
    return total_bits

def main():
    # Чтение содержимого файла text.txt
    with open('text.txt', 'r') as file:
        input_string = file.read()
    
    # Сжатие данных с использованием LZW
    compressed_data = lzw_compress(input_string)
    
    # Вычисление количества закодированных бит
    total_bits = calculate_encoded_bits(compressed_data)
    
    print(f'Количество закодированных бит: {total_bits}')

if __name__ == "__main__":
    main()
