# Turchanov Denis 4PM
# remake

"""Создаем класс шаблонный Array3d<> который хранит
одномерный массив, но выдаёт наружу его как трехмерный.
Переопрделеить операторы индексации (то есть array[i][j][k]),
Сделать методы GetValue0(int i) ->
GetValue1 (int j) ->[00
GetValues2(int k) -> [00
GetValues01 (int i, int j) -> [
GetValues02(int i, int k) ->[]
GetValues12(in j, int k) ->
Эти методы можно объединить в getValue(int i, int j, int k), где в случае, если индекс равен null, то он считается отсутсвующим
и аналогичные методы для SetValues
Сделать статический метод CreateFill для создания массива и
присваивания всех элементов одному значению"""


class Array3D:
    def __init__(self, size_i, size_j, size_k, default_value=None):
        self.size_i = size_i
        self.size_j = size_j
        self.size_k = size_k
        self.array = [default_value] * (size_i * size_j * size_k)

    def _get_index(self, i, j, k):
        return i * self.size_j * self.size_k + j * self.size_k + k

    def _is_index_valid(self, i, j, k):
        return 0 <= i < self.size_i and 0 <= j < self.size_j and 0 <= k < self.size_k

    def __getitem__(self, key):
        i, j, k = key
        if self._is_index_valid(i, j, k):
            return self.array[self._get_index(i, j, k)]
        else:
            return None

    def __setitem__(self, key, value):
        i, j, k = key
        if self._is_index_valid(i, j, k):
            self.array[self._get_index(i, j, k)] = value

    def GetValue0(self, i):
        return self[i, 0, 0]

    def GetValue1(self, j):
        return self[0, j, 0]

    def GetValue2(self, k):
        return self[0, 0, k]

    def GetValue01(self, i, j):
        return self[i, j, 0]

    def GetValue02(self, i, k):
        return self[i, 0, k]

    def GetValue12(self, j, k):
        return self[0, j, k]

    def setValue(self, i, j, k, value):
        self[i, j, k] = value

    @staticmethod
    def CreateFill(size_i, size_j, size_k, fill_value):
        return Array3D(size_i, size_j, size_k, default_value=fill_value)


arr = Array3D(3, 3, 3, default_value=0)

arr[1, 1, 1] = 42

# Получение значений
print(arr[1, 1, 1])  # Вывод: 42
print(arr.GetValue0(1))  # Вывод: 0
print(arr.GetValue01(1, 1))  # Вывод: 42

# Создание массива и заполнение значениями
arr_filled = Array3D.CreateFill(2, 2, 2, fill_value=10)
print(arr_filled[0, 0, 0])  # Вывод: 10

