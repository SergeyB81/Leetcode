class TimSort:
    """
    TIMSORT

    Смысл: Гибридный алгоритм, сочетающий сортировку вставками (для маленьких блоков)
    и сортировку слиянием (для объединения блоков). Разработан Тимо Петерсом для Python.

    Преимущества:
    - Оптимизирован для реальных данных (частично отсортированных)
    - Стабильная сортировка
    - Отличная производительность на всех типах данных
    - Используется как стандартная сортировка в Python, Java, Android

    Недостатки:
    - Сложная реализация
    - Требует O(n) дополнительной памяти
    - Избыточен для маленьких массивов

    Сложность: O(n log n) в среднем, O(n) для частично отсортированных
    Память: O(n)
    """

    # Минимальный размер блока (в реальном Timsort он вычисляется динамически)
    MIN_MERGE = 32

    def sort(self, arr):
        """
        Основной метод сортировки

        Args:
            arr: список для сортировки

        Returns:
            отсортированный список
        """
        n = len(arr)

        # Если массив маленький, используем сортировку вставками
        if n < self.MIN_MERGE:
            self._insertion_sort(arr, 0, n)
            return arr

        # Разбиваем массив на блоки (run'ы) и сортируем каждый вставками
        runs = []
        i = 0
        while i < n:
            # Определяем длину следующего блока
            run_start = i
            run_end = self._find_next_run(arr, i)

            # Сортируем блок вставками
            self._insertion_sort(arr, run_start, run_end)

            # Добавляем блок в список
            runs.append((run_start, run_end))
            i = run_end

        # Сливаем блоки, пока не останется один
        while len(runs) > 1:
            new_runs = []

            for j in range(0, len(runs), 2):
                if j + 1 < len(runs):
                    # Сливаем два соседних блока
                    left_start, left_end = runs[j]
                    right_start, right_end = runs[j + 1]

                    # Выполняем слияние
                    self._merge(arr, left_start, left_end, right_end)

                    # Добавляем объединенный блок
                    new_runs.append((left_start, right_end))
                else:
                    new_runs.append(runs[j])

            runs = new_runs

        return arr

    def _find_next_run(self, arr, start):
        """
        Находит следующий естественно отсортированный блок (run)
        Определяет направление сортировки и разворачивает если нужно
        """
        n = len(arr)
        if start >= n - 1:
            return n

        # Определяем направление
        if arr[start] <= arr[start + 1]:
            # Возрастающий порядок
            end = start + 1
            while end < n - 1 and arr[end] <= arr[end + 1]:
                end += 1
            return end + 1
        else:
            # Убывающий порядок - разворачиваем
            end = start + 1
            while end < n - 1 and arr[end] >= arr[end + 1]:
                end += 1

            # Разворачиваем убывающую последовательность
            left, right = start, end
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

            return end + 1

    def _insertion_sort(self, arr, left, right):
        """
        Сортировка вставками для подмассива [left, right)
        Используется для маленьких блоков
        """
        for i in range(left + 1, right):
            key = arr[i]
            j = i - 1

            # Сдвигаем элементы, пока не найдем место для key
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key

    def _merge(self, arr, left, mid, right):
        """
        Слияние двух отсортированных блоков:
        [left, mid) и [mid, right)
        """
        # Создаем временные копии
        left_part = arr[left:mid].copy()
        right_part = arr[mid:right].copy()

        i = j = 0
        k = left

        # Сливаем обратно
        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        # Добавляем остатки
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1


# Пример использования
if __name__ == "__main__":
    # Тестовые данные разных типов
    print("=== TEСТЫ TIMSORT ===\n")

    sorter = TimSort()

    # 1. Случайный массив
    random_array = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print(f"1. Случайный массив: {random_array}")
    result = sorter.sort(random_array.copy())
    print(f"   Результат: {result}")

    # 2. Частично отсортированный массив (сильная сторона Timsort)
    nearly_sorted = [1, 2, 3, 4, 5, 6, 10, 9, 8, 7, 11, 12, 13]
    print(f"\n2. Частично отсортированный: {nearly_sorted}")
    result = sorter.sort(nearly_sorted.copy())
    print(f"   Результат: {result}")

    # 3. Убывающий массив (будет развернут)
    descending = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"\n3. Убывающий массив: {descending}")
    result = sorter.sort(descending.copy())
    print(f"   Результат: {result}")

    # 4. Массив с повторяющимися элементами
    duplicates = [5, 2, 5, 3, 5, 1, 2, 5, 3, 2]
    print(f"\n4. С повторениями: {duplicates}")
    result = sorter.sort(duplicates.copy())
    print(f"   Результат: {result}")

    # Демонстрация поиска естественных блоков
    print("\n--- Демонстрация поиска блоков ---")
    demo = [1, 2, 3, 7, 6, 5, 4, 8, 9, 10]
    print(f"Исходные данные: {demo}")

    i = 0
    while i < len(demo):
        run_end = sorter._find_next_run(demo, i)
        print(f"  Блок [{i}:{run_end}]: {demo[i:run_end]}")
        i = run_end
