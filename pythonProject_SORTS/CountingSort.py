class CountingSort:
    """
    СОРТИРОВКА ПОДСЧЕТОМ (Counting Sort)

    Смысл: Для каждого элемента подсчитывается, сколько раз он встречается в массиве,
    затем на основе этих подсчетов определяется позиция каждого элемента.

    Преимущества:
    - Линейная сложность O(n + k) (где k - диапазон значений)
    - Стабильная сортировка
    - Очень быстрая для целых чисел в узком диапазоне
    - Не использует сравнения элементов

    Недостатки:
    - Требует дополнительной памяти O(k)
    - Работает только с дискретными значениями (целые числа)
    - Неэффективна при большом диапазоне значений
    - Не работает с числами с плавающей точкой (без модификации)

    Сложность: O(n + k) всегда
    Память: O(k) дополнительной памяти
    """

    def sort(self, arr):
        """
        Базовая версия для неотрицательных целых чисел

        Args:
            arr: список неотрицательных целых чисел

        Returns:
            отсортированный список
        """
        if not arr:
            return arr

        # Находим максимальное значение
        max_val = max(arr)

        # Создаем счетчик
        count = [0] * (max_val + 1)

        # Подсчитываем количество каждого элемента
        for num in arr:
            count[num] += 1

        # Восстанавливаем отсортированный массив
        result = []
        for i in range(max_val + 1):
            result.extend([i] * count[i])

        return result

    def sort_with_negative(self, arr):
        """
        Версия, поддерживающая отрицательные числа
        """
        if not arr:
            return arr

        # Находим минимум и максимум
        min_val = min(arr)
        max_val = max(arr)

        # Диапазон значений
        range_size = max_val - min_val + 1

        # Создаем счетчик со смещением
        count = [0] * range_size

        # Подсчет со смещением
        for num in arr:
            count[num - min_val] += 1

        # Восстанавливаем массив
        result = []
        for i in range(range_size):
            result.extend([i + min_val] * count[i])

        return result

    def sort_stable(self, arr):
        """
        Стабильная версия, сохраняющая порядок равных элементов
        (полезна для сортировки объектов по ключу)
        """
        if not arr:
            return arr

        # Находим диапазон
        min_val = min(arr)
        max_val = max(arr)
        range_size = max_val - min_val + 1

        # Счетчик
        count = [0] * range_size

        # Первый проход: подсчет
        for num in arr:
            count[num - min_val] += 1

        # Второй проход: вычисляем позиции (cumulative sum)
        for i in range(1, range_size):
            count[i] += count[i - 1]

        # Создаем результат и заполняем с конца (для стабильности)
        result = [0] * len(arr)

        # Идем с конца, чтобы сохранить порядок
        for num in reversed(arr):
            idx = num - min_val
            count[idx] -= 1
            result[count[idx]] = num

        return result

    def sort_by_key(self, items, key_func):
        """
        Сортировка объектов по целочисленному ключу

        Args:
            items: список объектов
            key_func: функция, возвращающая целочисленный ключ для объекта

        Returns:
            отсортированный список объектов
        """
        if not items:
            return items

        # Получаем все ключи
        keys = [key_func(item) for item in items]

        # Находим диапазон ключей
        min_key = min(keys)
        max_key = max(keys)
        range_size = max_key - min_key + 1

        # Счетчик
        count = [0] * range_size

        # Подсчет ключей
        for key in keys:
            count[key - min_key] += 1

        # Накопительные суммы
        for i in range(1, range_size):
            count[i] += count[i - 1]

        # Размещаем объекты
        result = [None] * len(items)
        for i in range(len(items) - 1, -1, -1):
            key = keys[i]
            idx = key - min_key
            count[idx] -= 1
            result[count[idx]] = items[i]

        return result

    def sort_strings_by_length(self, strings):
        """
        Сортировка строк по их длине
        """
        if not strings:
            return strings

        # Находим длины строк
        lengths = [len(s) for s in strings]
        min_len = min(lengths)
        max_len = max(lengths)
        range_size = max_len - min_len + 1

        # Счетчик
        count = [0] * range_size

        # Подсчет длин
        for length in lengths:
            count[length - min_len] += 1

        # Накопительные суммы
        for i in range(1, range_size):
            count[i] += count[i - 1]

        # Размещаем строки
        result = [None] * len(strings)
        for i in range(len(strings) - 1, -1, -1):
            length = lengths[i]
            idx = length - min_len
            count[idx] -= 1
            result[count[idx]] = strings[i]

        return result


# Пример использования
if __name__ == "__main__":
    print("=== СОРТИРОВКА ПОДСЧЕТОМ ===\n")

    sorter = CountingSort()

    # 1. Простые числа
    simple_data = [4, 2, 2, 8, 3, 3, 1, 5, 4, 2]
    print(f"1. Простые числа: {simple_data}")
    result = sorter.sort(simple_data)
    print(f"   Результат: {result}")

    # 2. С отрицательными числами
    negative_data = [5, -3, 2, -1, 0, -2, 4, 1, -4, 3]
    print(f"\n2. С отрицательными: {negative_data}")
    result = sorter.sort_with_negative(negative_data)
    print(f"   Результат: {result}")

    # 3. Стабильная сортировка объектов
    print("\n3. Стабильная сортировка объектов:")
    students = [
        ("Анна", 85),
        ("Иван", 75),
        ("Мария", 85),
        ("Петр", 90),
        ("Елена", 75)
    ]
    print(f"   Студенты: {students}")

    # Сортируем по баллам (второй элемент)
    sorted_students = sorter.sort_by_key(students, lambda s: s[1])
    print(f"   По баллам: {sorted_students}")
    print(f"   (заметьте: Анна и Мария с баллом 85 сохранили порядок)")

    # 4. Сортировка строк по длине
    strings = ["яблоко", "кот", "апельсин", "дом", "университет", "лес"]
    print(f"\n4. Строки: {strings}")
    sorted_strings = sorter.sort_strings_by_length(strings)
    print(f"   По длине: {sorted_strings}")

    # 5. Демонстрация процесса
    print("\n--- Процесс работы ---")
    demo = [4, 2, 2, 8, 3, 3, 1]
    print(f"Исходные данные: {demo}")
    print(f"Максимум: {max(demo)}")

    # Создаем счетчик
    count = [0] * (max(demo) + 1)
    for num in demo:
        count[num] += 1
    print(f"Счетчик: {count}")

    # Восстанавливаем
    result = []
    for i, c in enumerate(count):
        if c > 0:
            result.extend([i] * c)
            print(f"  Добавляем {c} раз число {i}")
    print(f"Результат: {result}")