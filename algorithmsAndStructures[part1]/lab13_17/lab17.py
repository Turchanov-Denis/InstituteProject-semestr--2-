class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
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

        root.key = minValueNode(root.right)
        root.right = delete(root.right, root.key)

    return root


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.key


def search(root, key):
    if root is None or root.key == key:
        return root

    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=' ')
        inorder_traversal(root.right)


def menu():
    return input("Меню:\n1. Добавить вершину\n2. Удалить вершину\n3. Поиск вершины\n4. Вывести БДП\n5. Выход\nВыберите операцию: ")


def main():
    root = None

    while True:
        choice = menu()

        if choice == '1':
            key = int(input("Введите значение вершины: "))
            root = insert(root, key)
        elif choice == '2':
            key = int(input("Введите значение вершины для удаления: "))
            root = delete(root, key)
        elif choice == '3':
            key = int(input("Введите значение вершины для поиска: "))
            result = search(root, key)
            if result:
                print(f"Вершина с ключом {key} найдена.")
            else:
                print(f"Вершина с ключом {key} не найдена.")
        elif choice == '4':
            print("БДП:")
            inorder_traversal(root)
            print()
        elif choice == '5':
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
