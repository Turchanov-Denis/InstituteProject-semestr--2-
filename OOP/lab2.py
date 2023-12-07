# Turchanov Denis 4PM

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


class Array3d:
    def __init__(self, size):
        self.size = size
        self.array = [
            [[None] * size for _ in range(size)] for _ in range(size)]

    def __getitem__(self, i):
        return self.array[i]

    def __setitem__(self, i, value):
        self.array[i] = value

    def GetValue0(self, i):
        return self.array[i]

    def GetValue1(self, j):
        return [row[j] for row in self.array]

    def GetValue2(self, k):
        return [[cell[k] for cell in row] for row in self.array]

    def GetValue01(self, i, j):
        return self.array[i][j]

    def GetValue02(self, i, k):
        return [cell[k] for cell in self.array[i]]

    def GetValue12(self, j, k):
        return [row[k] for row in self.array[j]]

    def getValue(self, i, j, k):
        if self.array[i] is None or self.array[i][j] is None or self.array[i][j][k] is None:
            return None
        return self.array[i][j][k]

    def SetValue(self, i, j, k, value):
        if self.array[i] is None:
            self.array[i] = []
        if self.array[i][j] is None:
            self.array[i][j] = []
        self.array[i][j][k] = value

    @staticmethod
    def CreateFill(size, value):
        return Array3d(size).fill(value)

    def fill(self, value):
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    self.array[i][j][k] = value
        return self


# Пример использования
arr = Array3d.CreateFill(3, 0)

print(arr[0][1][2])  # Output: 0
arr[0][1][2] = 5
print(arr[0][1][2])  # Output: 5

print(arr.GetValue0(0))  # Output: [0, 5, 0]
print(arr.GetValue1(1))  # Output: [5, 5, 5]
print(arr.GetValue2(2))  # Output: [[0, 5, 0], [0, 5, 0], [0, 5, 0]]
print(arr.GetValue01(0, 1))  # Output: 5
print(arr.GetValue02(0, 2))  # Output: [0, 5, 0]
print(arr.GetValue12(1, 2))  # Output: [5, 5, 5]
print(arr.getValue(0, 1, 2))  # Output: 5
