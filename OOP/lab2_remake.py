class Array3D:
    def __init__(self, first_dim, second_dim, third_dim):
        self._dimensions = {
            "first": first_dim,
            "second": second_dim,
            "third": third_dim
        }
        self._array = [None] * (first_dim * second_dim * third_dim)

    def _get_pointer(self, i, j, k):
        return i * self._dimensions["second"] * self._dimensions["third"] + j * self._dimensions["third"] + k

    def _check_dimensions(self, array, dim_size, dim_name):
        if len(array) != dim_size:
            raise ValueError(f"Размер массива для {dim_name} размерности не равен размеру {dim_name} размерности")

    def _set_values_01(self, array, i, j):
        for k in range(self._dimensions["third"]):
            self._array[self._get_pointer(i, j, k)] = array[k]

    def _set_values_02(self, array, i, k):
        for j in range(self._dimensions["second"]):
            self._array[self._get_pointer(i, j, k)] = array[j]

    def _set_values_12(self, array, j, k):
        for i in range(self._dimensions["first"]):
            self._array[self._get_pointer(i, j, k)] = array[i]

    def _set_values_0(self, two_dim_array, i):
        self._check_dimensions(two_dim_array, self._dimensions["second"], "второй")
        for j, sub_array in enumerate(two_dim_array):
            self._check_dimensions(sub_array, self._dimensions["third"], "третьей")
            self._set_values_01(sub_array, i, j)

    def _set_values_1(self, two_dim_array, j):
        self._check_dimensions(two_dim_array, self._dimensions["first"], "первой")
        for i, sub_array in enumerate(two_dim_array):
            self._check_dimensions(sub_array, self._dimensions["third"], "третьей")
            self._set_values_01(sub_array, i, j)

    def _set_values_2(self, two_dim_array, k):
        self._check_dimensions(two_dim_array, self._dimensions["first"], "первой")
        for i, sub_array in enumerate(two_dim_array):
            self._check_dimensions(sub_array, self._dimensions["second"], "второй")
            self._set_values_02(sub_array, i, k)

    def set_values(self, array, i=None, j=None, k=None):
        if i is not None and j is not None and k is not None:
            self._array[self._get_pointer(i, j, k)] = array
        elif i is not None and j is not None:
            self._set_values_01(array, i, j)
        elif i is not None and k is not None:
            self._set_values_02(array, i, k)
        elif j is not None and k is not None:
            self._set_values_12(array, j, k)
        elif i is not None:
            self._set_values_0(array, i)
        elif j is not None:
            self._set_values_1(array, j)
        elif k is not None:
            self._set_values_2(array, k)
        else:
            raise ValueError("Не указаны индексы для установки значений")

    def get(self, i=None, j=None, k=None):
        if i is not None and j is not None and k is not None:
            return self._array[self._get_pointer(i, j, k)]
        elif i is not None and j is not None:
            return self._get_values_01(i, j)
        elif i is not None and k is not None:
            return self._get_values_02(i, k)
        elif j is not None and k is not None:
            return self._get_values_12(j, k)
        elif i is not None:
            return self._get_values_0(i)
        elif j is not None:
            return self._get_values_1(j)
        elif k is not None:
            return self._get_values_2(k)
        else:
            raise ValueError("Не указаны индексы для получения значений")

    def create_fill(self, value):
        self._array = [value] * len(self._array)

    def get_size(self):
        return self._dimensions

    def __str__(self):
        result = "[\n"
        for i in range(self._dimensions["first"]):
            result += "  [\n"
            for j in range(self._dimensions["second"]):
                result += "    ["
                for k in range(self._dimensions["third"]):
                    value = self._array[self._get_pointer(i, j, k)]
                    result += " " + str(value) + ","
                result = result.rstrip(",") + " ],\n"
            result = result.rstrip(",\n") + "\n  ],\n"
        result = result.rstrip(",\n") + "\n]"
        return result


# Пример использования класса Array3D
array = Array3D(2, 3, 4)
print("Пустой массив:", array, "\n")

# Заполнение через create_fill()
array.create_fill(10)
print("Создаем заполнение:", array, "\n")

# Заполним массив значениями суммы индексов i+j+k
sizes = array.get_size()
for i in range(sizes["first"]):
    for j in range(sizes["second"]):
        for k in range(sizes["third"]):
            array.set_values(i + j + k, i, j, k)
print("i+j+k:", array, "\n")

try:
    array.set_values([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]], i=0)
    array.set_values([[3, 3, 3, 3], [4, 4, 4, 4]], j=1)
    array.set_values([[None, None, None], [None, None, None]], k=2)
    array.set_values([5, 5, 5, 5], i=1, j=0)
    array.set_values([6, 6], j=2, k=0)
    array.set_values([7, 7, 7], i=1, k=1)
except ValueError as error:
    print(error)

print("set_values():", array)