# Turchanov Denis 4PM
"""Создать 3 интерфейса: iNotifyPropertyChanged (уведомление при изменении поля в классе).
iNotifyPropertyChanging (уведомление о том, что сейчас вызвано изменение поля в классе, то есть что СЕЙЧАС произойдет изменение) и iNotifyCollectionChanged (уведомление об изменении состояния коллекции: Added- добавление нового элемента: Removed - удаление существующего элемента: Changed - изменение существующего элемента)
У каждого такого интерфейса должен быть метод для подключения (добавления к классу), который называется add А также метод отключения (удаления из класса), который называется remove"""

from abc import ABC, abstractmethod

class INotifyPropertyChanged(ABC):
    @abstractmethod
    def add_listener(self, callback):
        pass

    @abstractmethod
    def remove_listener(self, callback):
        pass


class INotifyPropertyChanging(ABC):
    @abstractmethod
    def add_listener(self, callback):
        pass

    @abstractmethod
    def remove_listener(self, callback):
        pass


class INotifyCollectionChanged(ABC):
    ADDED = "Added"
    REMOVED = "Removed"
    CHANGED = "Changed"

    @abstractmethod
    def add_listener(self, callback):
        pass

    @abstractmethod
    def remove_listener(self, callback):
        pass


class Collection(INotifyPropertyChanged, INotifyPropertyChanging, INotifyCollectionChanged):
    def __init__(self):
        self._listeners = {
            INotifyPropertyChanged: {"Changed": []},
            INotifyPropertyChanging: {"Changing": []},
            INotifyCollectionChanged: {"Added": [], "Removed": [], "Changed": []}
        }
        self._elements = []

    def add_element(self, element):
        changing = False

        # Notify Property Changing
        if changing:
            self._notify_property_changing()

        self._elements.append(element)

        self._notify_property_changed()

        # Notify Collection Changed (Added)
        self._notify_collection_changed(INotifyCollectionChanged.ADDED)

    def _notify_property_changed(self):
        for listener in self._listeners[INotifyPropertyChanged]["Changed"]:
            listener()

    def _notify_property_changing(self):
        for listener in self._listeners[INotifyPropertyChanging]["Changing"]:
            listener()

    def _notify_collection_changed(self, change_type):
        for listener in self._listeners[INotifyCollectionChanged][change_type]:
            listener()

    def add_listener(self, interface, change_type, callback):
        if interface in self._listeners and change_type in self._listeners[interface]:
            self._listeners[interface][change_type].append(callback)

    def remove_listener(self, interface, change_type, callback):
        if interface in self._listeners and change_type in self._listeners[interface]:
            self._listeners[interface][change_type].remove(callback)


# Пример использования
def added_callback():
    print("Added!")


def changed_callback():
    print("Changed!")


collection = Collection()

collection.add_listener(INotifyCollectionChanged, INotifyCollectionChanged.ADDED, added_callback)
collection.add_listener(INotifyCollectionChanged, INotifyCollectionChanged.CHANGED, changed_callback)

collection.add_element(123)
