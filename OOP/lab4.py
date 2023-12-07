# Turchanov Denis 4PM
import keyboard
import time

# Определение класса для клавиши на виртуальной клавиатуре.


class Key:
    def __init__(self, name, action, undo_action):
        self.name = name            # Имя или обозначение клавиши.
        # Действие, выполняемое при нажатии клавиши.
        self.action = action
        # Действие для отмены предыдущего действия.
        self.undo_action = undo_action

    # Метод для нажатия на клавишу.
    def press(self):
        return self.action()

    # Метод для отмены действия.
    def undo(self):
        return self.undo_action()

# Определение класса для виртуальной клавиатуры.


class KeyboardApp:
    def __init__(self):
        self.keys = {}              # Словарь для хранения всех клавиш.
        self.history = []           # Список для хранения истории действий.
        self.text = ""              # Строка для ввода текста.
        self.volume = 50            # Начальное значение громкости.

    # Метод для добавления клавиши на виртуальную клавиатуру.
    def addKey(self, key):
        self.keys[key.name] = key

    # Метод для имитации нажатия клавиши.
    def press(self, keyName):
        if keyName in self.keys:   # Если такая клавиша существует...
            result = self.keys[keyName].press()
            if result:
                # Добавляем действие в историю.
                self.history.append((self.keys[keyName], result))
            # Выводим текущее состояние.
            self.print_state()

    # Метод для отмены последнего действия.
    def undo(self):
        if self.history:
            key, prev_state = self.history[-1]
            key.undo()
            self.history.pop()     # Удаляем последний элемент из истории.
            self.print_state()     # Выводим текущее состояние.

    # Метод для вывода текущего состояния.
    def print_state(self):
        print(f"\nТекст: {self.text}")
        print(f"Громкость: {self.volume}\n")

# Основная функция программы.


def run():
    app = KeyboardApp()

    # Функции для действий и их отмены.
    def add_letter(letter):
        app.text += letter
        return app.text

    def delete_last_letter():
        app.text = app.text[:-1]
        return app.text

    def increase_volume():
        if app.volume < 100:
            app.volume += 10
        return app.volume

    def decrease_volume():
        if app.volume > 0:
            app.volume -= 10
        return app.volume

    # Добавляем буквенные клавиши на виртуальную клавиатуру.
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        app.addKey(
            Key(letter, lambda l=letter: add_letter(l), delete_last_letter))

    # Добавляем клавишу для регулировки громкости.
    app.addKey(Key("f8", increase_volume, decrease_volume))

    # Отслеживаем реальные нажатия клавиш и связываем их с действиями на виртуальной клавиатуре.
    for key in app.keys:
        keyboard.add_hotkey(key, lambda k=key: app.press(k))

    # Добавляем комбинацию для отмены последнего действия.
    keyboard.add_hotkey('ctrl+z', app.undo)

    print("Нажимайте клавиши для демонстрации. Для выхода нажмите ESC.")
    keyboard.wait('esc')  # Ожидаем нажатие клавиши ESC для завершения.


# Запускаем основную функцию.
run()
