# Интерфейс уведомления об изменении свойства
class INotifyPropertyChanged:
    def add_listener(self, listener):
        pass

    def remove_listener(self, listener):
        pass


# Интерфейс уведомления о предстоящем изменении свойства
class INotifyPropertyChanging:
    def add_listener(self, listener):
        pass

    def remove_listener(self, listener):
        pass


# Интерфейс уведомления об изменении коллекции
class INotifyCollectionChanged:
    def add_listener(self, listener):
        pass

    def remove_listener(self, listener):
        pass


# Класс, реализующий коллекцию
class Collection(INotifyCollectionChanged):
    def __init__(self):
        self.elements = []
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def remove_listener(self, listener):
        self.listeners.remove(listener)

    def add_element(self, element):
        for listener in self.listeners:
            listener(f"Added element {element}")

        self.elements.append(element)

    def change_element(self, index, element):
        for listener in self.listeners:
            listener(f"Changed element {self.elements[index]}. New element: {element}")

        self.elements[index] = element

    def remove_element(self, element):
        for listener in self.listeners:
            listener(f"Removed element {element}")

        self.elements.remove(element)


# Класс, реализующий изменение свойства и предстоящее изменение свойства
class First(INotifyPropertyChanged, INotifyPropertyChanging):
    def __init__(self):
        self._check = 0
        self.property_changed_listeners = []
        self.property_changing_listeners = []

    def add_property_changed_listener(self, listener):
        self.property_changed_listeners.append(listener)

    def remove_property_changed_listener(self, listener):
        self.property_changed_listeners.remove(listener)

    def add_property_changing_listener(self, listener):
        self.property_changing_listeners.append(listener)

    def remove_property_changing_listener(self, listener):
        self.property_changing_listeners.remove(listener)

    def set_check(self, new_value):
        old_value = self._check
        flag = True
        for listener in self.property_changing_listeners:
            if not listener("Check", old_value, new_value):
                flag = False
                break
        if flag:
            for listener in self.property_changed_listeners:
                listener("Check", old_value, new_value)
            self._check = new_value



def property_changed_handler(property_name, old_value, new_value):
    print(f"Property '{property_name}' changed from {old_value} to {new_value}")


def property_changing_handler(property_name, old_value, new_value):
    print(f"Property '{property_name}' changing from {old_value} to {new_value}")

def collection_changed_handler(status):
    print(f"Collection changed, status: {status}")


# Создание экземпляров классов
collection_instance = Collection()
first_instance = First()

# Подключение обработчиков событий
collection_instance.add_listener(collection_changed_handler)
first_instance.add_property_changed_listener(property_changed_handler)
first_instance.add_property_changing_listener(property_changing_handler)

# Изменение свойств и коллекции
collection_instance.add_element(123)
collection_instance.add_element(321)
collection_instance.change_element(0, 3456789)
collection_instance.remove_element(321)
