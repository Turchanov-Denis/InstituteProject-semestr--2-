# Turchanov Denis 4PM
"""Создать симуляцию крокссплатформенного приложения пр помощи паттерна 
«абстрактная фабрика». Фабрика должна генерировать набор контроллов для 
различных операционных систем (Windows, Linux, MacOS).
Все контроллы наследуются от базового класса 
Contol (setPosition, getPosition).
Примеры реализующихся контроллов и их возможных методов
Form (addContol)
Label (setText, getText)
TextBox (setText, getText, OnValueChanged)
ComboBox (getSeletecedIndex, setSelectedIndex, setItems, getItems)
Button (setText, getText, Click)
Приложение должно в зависимости от выбранной операционной системы 
создавать свой набор контроллов, размещать их на форме, делать с ними 
манипуляции (вызывать их методы(.
Графический интерфейс создавать не требуется! Контроллы в реальности на 
все методы просто пишут информацию о вызове метода в консоль по типу:
«Вызван метод _____  у контролла ___»"""
from abc import ABC, abstractmethod


class Control(ABC):
    @abstractmethod
    def setPosition(self, x, y):
        pass

    @abstractmethod
    def getPosition(self):
        pass


class Form(Control):
    def addControl(self, control):
        print(f"Добавлен контрол {control} на форму")

    def setPosition(self, x, y):
        print(f"Позиция установлена на ({x}, {y})")

    def getPosition(self):
        return "Текущая позиция"

# Классы для контролов: Label, TextBox, ComboBox, Button


class Label(Control):
    # Методы для управления текстовым полем Label
    def setText(self, text):
        print(f"Вызван метод setText у контролла Label")

    def getText(self):
        print(f"Вызван метод getText у контролла Label")
        return "Текст получен"

    def setPosition(self, x, y):
        print(f"Вызван метод setPosition у контролла Label: ({x}, {y})")

    def getPosition(self):
        print(f"Вызван метод getPosition у контролла Label")
        return "Текущая позиция"


class TextBox(Control):
    def setText(self, text):
        print(f"Вызван метод setText у контролла TextBox: {text}")

    def getText(self):
        print(f"Вызван метод getText у контролла TextBox")
        return "Текст получен"

    def OnValueChanged(self):
        print("Вызван метод OnValueChanged у контролла TextBox")

    def setPosition(self, x, y):
        print(f"Вызван метод setPosition у контролла TextBox: ({x}, {y})")

    def getPosition(self):
        print(f"Вызван метод getPosition у контролла TextBox")
        return "Текущая позиция"


class ComboBox(Control):
    def getSelectedIndex(self):
        print(f"Вызван метод getSelectedIndex у контролла ComboBox")
        return "Индекс выбранного элемента"

    def setSelectedIndex(self, index):
        print(f"Вызван метод setSelectedIndex у контролла ComboBox: {index}")

    def setItems(self, items):
        print(f"Вызван метод setItems у контролла ComboBox: {items}")

    def getItems(self):
        print(f"Вызван метод getItems у контролла ComboBox")
        return "Получены элементы"

    def setPosition(self, x, y):
        print(f"Вызван метод setPosition у контролла ComboBox: ({x}, {y})")

    def getPosition(self):
        print(f"Вызван метод getPosition у контролла ComboBox")
        return "Текущая позиция"


class Button(Control):
    def setText(self, text):
        print(f"Вызван метод setText у контролла Button: {text}")

    def getText(self):
        print(f"Вызван метод getText у контролла Button")
        return "Текст получен"

    def Click(self):
        print("Вызван метод Click у контролла Button")

    def setPosition(self, x, y):
        print(f"Вызван метод setPosition у контролла Button: ({x}, {y})")

    def getPosition(self):
        print(f"Вызван метод getPosition у контролла Button")
        return "Текущая позиция"


# Абстрактная фабрика для создания контролов
class GUIFactory(ABC):
    @abstractmethod
    def createLabel(self) -> Label:
        pass

    @abstractmethod
    def createTextBox(self) -> TextBox:
        pass

    @abstractmethod
    def createComboBox(self) -> ComboBox:
        pass

    @abstractmethod
    def createButton(self) -> Button:
        pass

# Фабрика для Windows


class WindowsFactory(GUIFactory):
    # Определения контролов для Windows
    class WindowsLabel(Label):
        def setPosition(self, x, y):
            print(f"Windows Label: setPosition({x}, {y})")

        def getPosition(self):
            return "Windows Label: getPosition"

    class WindowsTextBox(TextBox):
        def setPosition(self, x, y):
            print(f"Windows TextBox: setPosition({x}, {y})")

        def getPosition(self):
            return "Windows TextBox: getPosition"

        def OnValueChanged(self):
            print("Windows TextBox: OnValueChanged event")

    class WindowsComboBox(ComboBox):
        def setPosition(self, x, y):
            print(f"Windows ComboBox: setPosition({x}, {y})")

        def getPosition(self):
            return "Windows ComboBox: getPosition"

        def getSelectedIndex(self):
            return "Windows ComboBox: getSelectedIndex"

        def setSelectedIndex(self, index):
            print(f"Windows ComboBox: setSelectedIndex({index})")

        def setItems(self, items):
            print(f"Windows ComboBox: setItems({items})")

    class WindowsButton(Button):
        def setPosition(self, x, y):
            print(f"Windows Button: setPosition({x}, {y})")

        def getPosition(self):
            return "Windows Button: getPosition"

        def Click(self):
            print("Windows Button: Click event")

    def createLabel(self) -> Label:
        return self.WindowsLabel()

    def createTextBox(self) -> TextBox:
        return self.WindowsTextBox()

    def createComboBox(self) -> ComboBox:
        return self.WindowsComboBox()

    def createButton(self) -> Button:
        return self.WindowsButton()

# Фабрика для Linux


class LinuxFactory(GUIFactory):
    # Определения контролов для Linux
    class LinuxLabel(Label):
        def setPosition(self, x, y):
            print(f"Linux Label: setPosition({x}, {y})")

        def getPosition(self):
            return "Linux Label: getPosition"

    class LinuxTextBox(TextBox):
        def setPosition(self, x, y):
            print(f"Linux TextBox: setPosition({x}, {y})")

        def getPosition(self):
            return "Linux TextBox: getPosition"

        def OnValueChanged(self):
            print("Linux TextBox: OnValueChanged event")

    class LinuxComboBox(ComboBox):
        def setPosition(self, x, y):
            print(f"Linux ComboBox: setPosition({x}, {y})")

        def getPosition(self):
            return "Linux ComboBox: getPosition"

        def getSelectedIndex(self):
            return "Linux ComboBox: getSelectedIndex"

        def setSelectedIndex(self, index):
            print(f"Linux ComboBox: setSelectedIndex({index})")

        def setItems(self, items):
            print(f"Linux ComboBox: setItems({items})")

    class LinuxButton(Button):
        def setPosition(self, x, y):
            print(f"Linux Button: setPosition({x}, {y})")

        def getPosition(self):
            return "Linux Button: getPosition"

        def Click(self):
            print("Linux Button: Click event")

    def createLabel(self) -> Label:
        return self.LinuxLabel()

    def createTextBox(self) -> TextBox:
        return self.LinuxTextBox()

    def createComboBox(self) -> ComboBox:
        return self.LinuxComboBox()

    def createButton(self) -> Button:
        return self.LinuxButton()

# Фабрика для MacOS


class MacOSFactory(GUIFactory):
    # Определения контролов для MacOS
    class MacOSLabel(Label):
        def setPosition(self, x, y):
            print(f"MacOS Label: setPosition({x}, {y})")

        def getPosition(self):
            return "MacOS Label: getPosition"

    class MacOSTextBox(TextBox):
        def setPosition(self, x, y):
            print(f"MacOS TextBox: setPosition({x}, {y})")

        def getPosition(self):
            return "MacOS TextBox: getPosition"

        def OnValueChanged(self):
            print("MacOS TextBox: OnValueChanged event")

    class MacOSComboBox(ComboBox):
        def setPosition(self, x, y):
            print(f"MacOS ComboBox: setPosition({x}, {y})")

        def getPosition(self):
            return "MacOS ComboBox: getPosition"

        def getSelectedIndex(self):
            return "MacOS ComboBox: getSelectedIndex"

        def setSelectedIndex(self, index):
            print(f"MacOS ComboBox: setSelectedIndex({index})")

        def setItems(self, items):
            print(f"MacOS ComboBox: setItems({items})")

    class MacOSButton(Button):
        def setPosition(self, x, y):
            print(f"MacOS Button: setPosition({x}, {y})")

        def getPosition(self):
            return "MacOS Button: getPosition"

        def Click(self):
            print("MacOS Button: Click event")

    def createLabel(self) -> Label:
        return self.MacOSLabel()

    def createTextBox(self) -> TextBox:
        return self.MacOSTextBox()

    def createComboBox(self) -> ComboBox:
        return self.MacOSComboBox()

    def createButton(self) -> Button:
        return self.MacOSButton()


# Функция выбора операционной системы
def select_operating_system():
    print("Выберите операционную систему:")
    print("1. Windows")
    print("2. Linux")
    print("3. MacOS")
    choice = input("Введите номер: ")

    if choice == '1':
        return WindowsFactory()  # Возвращаем фабрику для Windows
    elif choice == '2':
        return LinuxFactory()    # Возвращаем фабрику для Linux
    elif choice == '3':
        return MacOSFactory()    # Возвращаем фабрику для MacOS
    else:
        print("Неверный выбор, используется фабрика для Windows по умолчанию")
        return WindowsFactory()  # Возвращаем фабрику для Windows по умолчанию

# Главная функция приложения


def run_application():
    factory = select_operating_system()  # Выбор фабрики в зависимости от ОС
    form = Form()  # Создание формы

    # Создание контролов для формы с помощью выбранной фабрики
    label = factory.createLabel()
    textbox = factory.createTextBox()
    combobox = factory.createComboBox()
    button = factory.createButton()

    # Добавление созданных контролов на форму
    form.addControl(label)
    form.addControl(textbox)
    form.addControl(combobox)
    form.addControl(button)

    # Вызов методов контролов
    label.setPosition(10, 20)
    print(label.getPosition())

    textbox.setPosition(30, 40)
    print(textbox.getPosition())
    textbox.setText("Hello")
    print(textbox.getText())

    combobox.setPosition(50, 60)
    print(combobox.getPosition())
    combobox.setItems(["Item 1", "Item 2", "Item 3"])
    combobox.setSelectedIndex(1)
    print(combobox.getSelectedIndex())

    button.setPosition(70, 80)
    print(button.getPosition())
    button.Click()


# Запуск приложения
run_application()
