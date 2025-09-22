def move_zeros(nums):
    """
    Перемещает все нули в конец списка, сохраняя порядок ненулевых элементов.

    Args:
        nums: List[int] - список целых чисел

    Returns:
        List[int] - список с нулями в конце
    """
    # Указатель для позиции, куда вставлять ненулевые элементы
    insert_pos = 0

    # Первый проход: перемещаем все ненулевые элементы в начало
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    # Второй проход: заполняем оставшиеся позиции нулями
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

    return nums

# или

def move_zeros1(arr):
    zero_ind = None

    for i in range(len(arr)):
        if (arr[i] == 0) and (zero_ind is None):
            zero_ind = i
            continue

        if (zero_ind is not None) and (arr[i] != 0):
            arr[zero_ind], arr[i] = arr[i], arr[zero_ind]
            zero_ind += 1

    return arr  # Добавил возврат результата для тестирования



if __name__ == "__main__":
    # Пример из условия
    test_list = [1, 2, 3, 0, 0, 4, 0, 5]
    print(f"Исходный список: {test_list}")
    print(f"Результат: {move_zeros(test_list)}")

    # Дополнительные тесты
    print(f"Тест 2: {move_zeros([0, 1, 0, 3, 12])}")  # [1, 3, 12, 0, 0]
    print(f"Тест 3: {move_zeros([0, 0, 0, 1])}")  # [1, 0, 0, 0]
    print(f"Тест 4: {move_zeros([1, 2, 3])}")  # [1, 2, 3]
    print(f"Тест 5: {move_zeros([0, 0, 0])}")  # [0, 0, 0]

# rep 5