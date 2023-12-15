class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        root.key = minValueNode(root.right).key
        root.right = delete(root.right, root.key)

    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def search(root, key):
    if root is None or root.key == key:
        return root

    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.key))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L --- ")
            print_tree(node.right, level + 1, "R --- ")

def print_menu():
    print("\nМеню:")
    print("1. Добавить вершину")
    print("2. Удалить вершину")
    print("3. Найти вершину")
    print("4. Вывести БДП")
    print("5. Выйти")

def main():
    root = None

    while True:
        print_menu()
        choice = int(input("Выберите операцию (1-5): "))

        if choice == 1:
            key = int(input("Введите ключ для добавления: "))
            root = insert(root, key)
        elif choice == 2:
            key = int(input("Введите ключ для удаления: "))
            root = delete(root, key)
        elif choice == 3:
            key = int(input("Введите ключ для поиска: "))
            if search(root, key):
                print(f"Вершина с ключом {key} найдена в БДП.")
            else:
                print(f"Вершина с ключом {key} не найдена в БДП.")
        elif choice == 4:
            print("БДП (графический вывод):")
            print_tree(root)
        elif choice == 5:
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
