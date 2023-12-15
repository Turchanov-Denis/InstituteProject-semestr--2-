class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableWithCollision:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert_with_collision(self, key, value):
        index = self.hash_function(key)

        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))

    def display_table(self):
        for i in range(self.size):
            print(f'Index {i}: {self.table[i]}')

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for i in range(self.size):
                file.write(f'Index {i}: {self.table[i]}\n')


class HashTableWithLinkedList:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return len(key) % self.size

    def insert_with_collision(self, key, value):
        index = self.hash_function(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)

    def display_table(self):
        for i in range(self.size):
            current = self.table[i]
            values = []
            while current is not None:
                values.append((current.key, current.value))
                current = current.next
            print(f'Index {i}: {values}')

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for i in range(self.size):
                current = self.table[i]
                values = []
                while current is not None:
                    values.append((current.key, current.value))
                    current = current.next
                file.write(f'Index {i}: {values}\n')


def main():
    input_string = "8(3(1,6(4,7)),10(,14(13,)))"
    output_file_collision = "hash_table_with_collision.txt"
    output_file_linked_list = "hash_table_with_linked_list.txt"
    table_size = 10

    # Создаем хеш-таблицу с наложением
    table_with_collision = HashTableWithCollision(size=table_size)

    # Парсим символьную строку и добавляем элементы в хеш-таблицу с наложением
    for char in input_string:
        table_with_collision.insert_with_collision(char, char)

    # Выводим хеш-таблицу с наложением
    print("Хеш-таблица с наложением:")
    table_with_collision.display_table()

    # Записываем хеш-таблицу с наложением в файл
    table_with_collision.save_to_file(output_file_collision)
    print(f"Хеш-таблица с наложением сохранена в файл: {output_file_collision}")

    # Создаем хеш-таблицу со связанными списками
    table_with_linked_list = HashTableWithLinkedList(size=table_size)

    # Парсим символьную строку и добавляем элементы в хеш-таблицу со связанными списками
    for char in input_string:
        table_with_linked_list.insert_with_collision(char, char)

    # Выводим хеш-таблицу со связанными списками
    print("Хеш-таблица со связанными списками:")
    table_with_linked_list.display_table()

    # Записываем хеш-таблицу со связанными списками в файл
    table_with_linked_list.save_to_file(output_file_linked_list)
    print(f"Хеш-таблица со связанными списками сохранена в файл: {output_file_linked_list}")

if __name__ == "__main__":
    main()
