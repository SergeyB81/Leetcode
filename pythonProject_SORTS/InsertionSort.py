class InsertionSort:
    """
    СОРТИРОВКА ВСТАВКАМИ (Insertion Sort)

    Смысл: Алгоритм строит отсортированную последовательность, постепенно добавляя
    в неё элементы из неотсортированной части. Каждый новый элемент вставляется
    на правильную позицию в уже отсортированной части.

    Преимущества:
    - Простая и интуитивная реализация
    - Отличная производительность для маленьких массивов (до 100 элементов)
    - Эффективна для почти отсортированных данных (O(n))
    - Стабильная сортировка
    - Сортирует на месте
    - Адаптивна (использует существующий порядок)

    Недостатки:
    - Квадратичная сложность O(n²) для случайных данных
    - Неэффективна для больших массивов

    Сложность: O(n²) в среднем и худшем, O(n) в лучшем (уже отсортирован)
    Память: O(1) дополнительной памяти
    """

    def sort(self, arr):
        """
        Основной метод сортировки

        Args:
            arr: список для сортировки

        Returns:
            отсортированный список (тот же объект)
        """
        n = len(arr)

        # Начинаем со второго элемента (первый считаем отсортированным)
        for i in range(1, n):
            key = arr[i]  # элемент, который нужно вставить
            j = i - 1  # индекс последнего элемента в отсортированной части

            # Сдвигаем элементы отсортированной части вправо,
            # пока не найдем правильную позицию для key
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]  # сдвиг вправо
                j -= 1

            # Вставляем key на найденную позицию
            arr[j + 1] = key

            # Для отладки можно выводить каждый шаг
            # print(f"  Шаг {i}: вставляем {key} -> {arr}")

        return arr

    def sort_with_binary_search(self, arr):
        """
        Улучшенная версия с бинарным поиском позиции вставки
        Быстрее для больших массивов, но все равно O(n²) из-за сдвигов
        """
        n = len(arr)

        for i in range(1, n):
            key = arr[i]

            # Используем бинарный поиск для нахождения позиции вставки
            pos = self._binary_search(arr, key, 0, i)

            # Сдвигаем элементы для освобождения места
            for j in range(i, pos, -1):
                arr[j] = arr[j - 1]

            arr[pos] = key

        return arr

    def _binary_search(self, arr, key, left, right):
        """
        Бинарный поиск позиции для вставки key в отсортированном подмассиве
        """
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= key:
                left = mid + 1
            else:
                right = mid
        return left

    def sort_range(self, arr, left, right):
        """
        Сортировка только указанного диапазона [left, right)
        Полезно как подпрограмма для других алгоритмов
        """
        for i in range(left + 1, right):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def sort_descending(self, arr):
        """
        Сортировка по убыванию
        """
        n = len(arr)

        for i in range(1, n):
            key = arr[i]
            j = i - 1
            # Изменяем условие на противоположное
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr


# Пример использования
if __name__ == "__main__":
    # Тестовые данные
    test_array = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print(f"Исходный массив: {test_array}")

    # Создаем экземпляр сортировщика
    sorter = InsertionSort()

    # Обычная сортировка
    array_regular = test_array.copy()
    sorter.sort(array_regular)
    print(f"Обычная сортировка: {array_regular}")

    # Сортировка с бинарным поиском
    array_binary = test_array.copy()
    sorter.sort_with_binary_search(array_binary)
    print(f"С бинарным поиском: {array_binary}")

    # Сортировка по убыванию
    array_desc = test_array.copy()
    sorter.sort_descending(array_desc)
    print(f"По убыванию: {array_desc}")

    # Демонстрация эффективности на почти отсортированных данных
    print("\n--- Эффективность на почти отсортированных данных ---")
    nearly_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 14, 13, 12, 11]
    print(f"Почти отсортированный: {nearly_sorted}")

    # Покажем пошагово
    demo = nearly_sorted.copy()
    n = len(demo)
    print("\nПошаговый процесс:")
    for i in range(1, n):
        key = demo[i]
        j = i - 1
        print(f"  Шаг {i}: key = {key}")
        print(f"    До:    {demo}")

        while j >= 0 and demo[j] > key:
            demo[j + 1] = demo[j]
            j -= 1
        demo[j + 1] = key

        print(f"    После: {demo}")

    # Сравнение с полностью случайными данными
    print("\n--- Сравнение производительности ---")
    import time

    # Маленький массив (где вставки хороши)
    small_array = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    print(f"Маленький массив (9 элементов): {small_array}")

    start = time.time()
    sorter.sort(small_array.copy())
    time_small = time.time() - start
    print(f"  Время сортировки: {time_small:.6f} сек")

    # Почти отсортированный массив
    almost_sorted = list(range(1000)) + [999, 998, 997]  # почти отсортирован
    print(f"\nПочти отсортированный массив (1003 элемента)")

    start = time.time()
    sorter.sort(almost_sorted.copy())
    time_almost = time.time() - start
    print(f"  Время сортировки: {time_almost:.6f} сек")