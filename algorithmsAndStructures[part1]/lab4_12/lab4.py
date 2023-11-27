class SortingMethods:
    @staticmethod
    def comb_sort(ls):
        n = len(ls)
        step = n
        while step > 1 or flag:
            if step > 1:
                step = int(step / 1.247331)
            flag, i = False, 0
            while i + step < n:
                if ls[i] > ls[i + step]:
                    ls[i], ls[i + step] = ls[i + step], ls[i]
                    flag = True
                i += step
        return ls

    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr

    @staticmethod
    def selection_sort(arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr

    @staticmethod
    def shell_sort(arr):
        n = len(arr)
        step  = n // 2
        while step  > 0:
            for i in range(step , n):
                temp = arr[i]
                j = i
                while j >= step  and arr[j - step ] > temp:
                    arr[j] = arr[j - step ]
                    j -= step 
                arr[j] = temp
            step  //= 2
        return arr

    @staticmethod
    def radix_sort(arr):
        def counting_sort(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                index = arr[i] // exp
                count[index % 10] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1

            i = 0
            for i in range(n):
                arr[i] = output[i]

        max_element = max(arr)
        exp = 1
        while max_element // exp > 0:
            counting_sort(arr, exp)
            exp *= 10

        return arr

    @staticmethod
    def heap_sort(arr):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[i] < arr[left]:
                largest = left

            if right < n and arr[largest] < arr[right]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

        return arr

    @staticmethod
    def merge_sort(arr):
        def merge(arr, left, mid, right):
            n1 = mid - left + 1
            n2 = right - mid

            L = [0] * n1
            R = [0] * n2

            for i in range(n1):
                L[i] = arr[left + i]

            for j in range(n2):
                R[j] = arr[mid + 1 + j]

            i = j = 0
            k = left

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1

            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1

        def merge_sort_helper(arr, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort_helper(arr, left, mid)
                merge_sort_helper(arr, mid + 1, right)
                merge(arr, left, mid, right)

        merge_sort_helper(arr, 0, len(arr) - 1)
        return arr

    @staticmethod
    def quick_sort(arr):
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def quick_sort_helper(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quick_sort_helper(arr, low, pi - 1)
                quick_sort_helper(arr, pi + 1, high)

        quick_sort_helper(arr, 0, len(arr) - 1)
        return arr


def main():
    # Пример использования
    sequence = [64, 34, 25, 12, 22, 11, 90]

    sorting_instance = SortingMethods()

    # Примеры вызова различных методов сортировки
    comb_sorted = sorting_instance.comb_sort(sequence.copy())
    insertion_sorted = sorting_instance.insertion_sort(sequence.copy())
    selection_sorted = sorting_instance.selection_sort(sequence.copy())
    shell_sorted = sorting_instance.shell_sort(sequence.copy())
    radix_sorted = sorting_instance.radix_sort(sequence.copy())
    heap_sorted = sorting_instance.heap_sort(sequence.copy())
    merge_sorted = sorting_instance.merge_sort(sequence.copy())
    quick_sorted = sorting_instance.quick_sort(sequence.copy())
    # external_sorted = sorting_instance.external_sort(sequence.copy())  # Замените на свой код

    # Вывод результатов
    print("Original Sequence:", sequence)
    print("Comb Sort:", comb_sorted)
    print("Insertion Sort:", insertion_sorted)
    print("Selection Sort:", selection_sorted)
    print("Shell Sort:", shell_sorted)
    print("Radix Sort:", radix_sorted)
    print("Heap Sort:", heap_sorted)
    print("Merge Sort:", merge_sorted)
    print("Quick Sort:", quick_sorted)
    # print("External Sort:", external_sorted)

if __name__ == "__main__":
    main()