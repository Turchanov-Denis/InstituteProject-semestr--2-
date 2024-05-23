def count_bits(filename):
    try:
        with open(filename, 'rb') as file:
            file_content = file.read()
            num_bits = len(file_content) * 8
            return num_bits
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return None

filename = "text.txt"
num_bits = count_bits(filename)
if num_bits is not None:
    print(f"Количество бит в файле '{filename}': {num_bits}")
