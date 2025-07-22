def bubble_sort(arr):
    # O(n**2)
    swapped = False
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def selection_sort(arr):
    # O(n**2)
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    # O(n**2)
    for i in range(1, len(arr)):
        j = i - 1
        cur_el = arr[i]
        while j >= 0 and cur_el < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = cur_el  # insert


def quick_sort_op(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[-1]

    less = [el for el in arr[:-1] if el < pivot]
    greater = [el for el in arr[:-1] if el >= pivot]

    return quick_sort_op(less) + [pivot] + quick_sort_op(greater)


# Функция разбиения (partition)
def partition(arr, start, end):
    # Устанавливаем индекс для "меньшей" части массива
    i = start - 1

    # Выбираем опорный элемент (pivot) — последний элемент текущего подмассива
    pivot = arr[end]

    # Перебираем элементы с индекса start до end - 1
    for j in range(start, end):
        # Если текущий элемент меньше опорного
        if arr[j] < pivot:
            # Увеличиваем индекс меньшей части
            i = i + 1
            # Меняем местами текущий элемент и элемент на позиции i
            arr[i], arr[j] = arr[j], arr[i]

    # После завершения цикла:
    # Слева от i — элементы < pivot
    # Справа от i — элементы >= pivot
    # Помещаем опорный элемент в его окончательное место — на позицию i + 1
    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    # Возвращаем индекс, на котором теперь находится опорный элемент
    return i + 1


# Рекурсивная функция быстрой сортировки
def quick_sort(arr, start, end):
    # Базовое условие: если подмассив состоит из более чем одного элемента
    if start < end:
        # Выполняем разбиение и получаем индекс опорного элемента
        pi = partition(arr, start, end)

        # Рекурсивно сортируем левую часть (до опорного элемента)
        quick_sort(arr, start, pi - 1)

        # Рекурсивно сортируем правую часть (после опорного элемента)
        quick_sort(arr, pi + 1, end)




if __name__ == '__main__':
    print('sergey')
    nums = [4,8,0,10,2,1,3,2,9,7]
   # nums = [2,2,2,2]
    quick_sort(nums, 0, len(nums)-1)
   # insertion_sort(nums)
   # selection_sort(nums)
   # nums = [4, 8, 2, 1, 3]
   # bubble_sort(nums)
   # print(partition(nums, 0 ,6))
   # print(quick_sort(nums,0,9))
    print(nums)
# rep 5+