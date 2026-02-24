class ShellSort:
    """
    СОРТИРОВКА ШЕЛЛА (Shell Sort)

    Смысл: Улучшенная версия сортировки вставками, которая сравнивает и обменивает
    элементы, находящиеся на определенном расстоянии (gap). Постепенно gap уменьшается
    до 1, когда алгоритм становится обычной сортировкой вставками.

    Преимущества:
    - Быстрее простых квадратичных сортировок
    - Сортирует на месте (O(1) памяти)
    - Хорошо работает для средних массивов
    - Простая реализация
    - Не рекурсивна

    Недостатки:
    - Сложность зависит от выбора последовательности gap'ов
    - Нестабильная сортировка
    - Медленнее O(n log n) алгоритмов для больших массивов

    Сложность: O(n log² n) в среднем, зависит от последовательности gap'ов
    Память: O(1) дополнительной памяти
    """

    def __init__(self, gap_sequence="ciura"):
        """
        Args:
            gap_sequence: тип последовательности gap'ов
                "ciura" - последовательность Чиуры [1,4,10,23,57,132,...]
                "shell" - оригинальная последовательность Шелла n/2^k
                "hibbard" - последовательность Хиббарда 2^k-1
                "sedgewick" - последовательность Седжвика
                "fibonacci" - последовательность Фибоначчи
        """
        self.gap_sequence = gap_sequence

    def sort(self, arr):
        """
        Основной метод сортировки

        Args:
            arr: список для сортировки

        Returns:
            отсортированный список
        """
        n = len(arr)

        # Получаем последовательность gap'ов
        gaps = self._get_gap_sequence(n)

        # Для каждого gap
        for gap in gaps:
            # Выполняем сортировку вставками с шагом gap
            for i in range(gap, n):
                temp = arr[i]
                j = i

                # Сдвигаем элементы с шагом gap
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap

                arr[j] = temp

        return arr

    def _get_gap_sequence(self, n):
        """
        Генерирует последовательность gap'ов в убывающем порядке
        """
        gaps = []

        if self.gap_sequence == "ciura":
            # Последовательность Чиуры (эмпирически лучшая для n < 4000)
            all_gaps = [1750, 701, 301, 132, 57, 23, 10, 4, 1]
            # Оставляем только те, что меньше n
            gaps = [g for g in all_gaps if g < n]

        elif self.gap_sequence == "shell":
            # Оригинальная последовательность Шелла: n/2, n/4, n/8, ..., 1
            gap = n // 2
            while gap > 0:
                gaps.append(gap)
                gap //= 2

        elif self.gap_sequence == "hibbard":
            # Последовательность Хиббарда: 2^k - 1
            k = 1
            gaps_temp = []
            while True:
                gap = (1 << k) - 1  # 2^k - 1
                if gap >= n:
                    break
                gaps_temp.append(gap)
                k += 1
            gaps = sorted(gaps_temp, reverse=True)  # убывающий порядок

        elif self.gap_sequence == "sedgewick":
            # Последовательность Седжвика (исправленная версия)
            # Используем формулу: 4^k + 3*2^(k-1) + 1 для нечетных и 9*4^k - 9*2^k + 1 для четных
            gaps_temp = set()  # используем множество для избежания дубликатов

            k = 0
            while True:
                # Формула для нечетных: 4^k + 3*2^(k-1) + 1 (для k >= 1)
                if k >= 1:
                    gap1 = (1 << (2 * k)) + 3 * (1 << (k - 1)) + 1  # 4^k + 3*2^(k-1) + 1
                    if gap1 < n:
                        gaps_temp.add(gap1)

                # Формула для четных: 9*4^k - 9*2^k + 1
                gap2 = 9 * (1 << (2 * k)) - 9 * (1 << k) + 1  # 9*4^k - 9*2^k + 1
                if gap2 < n:
                    gaps_temp.add(gap2)
                else:
                    break

                k += 1

            # Добавляем 1, если её нет
            gaps_temp.add(1)

            # Сортируем по убыванию и фильтруем положительные
            gaps = sorted([g for g in gaps_temp if g > 0], reverse=True)

        elif self.gap_sequence == "fibonacci":
            # Последовательность Фибоначчи
            fib = [1, 1]
            while fib[-1] < n:
                fib.append(fib[-1] + fib[-2])
            # Берем числа Фибоначчи, меньшие n, в обратном порядке
            gaps = [f for f in reversed(fib) if f < n]

        # Убеждаемся, что последний gap = 1
        if gaps and gaps[-1] != 1:
            gaps.append(1)

        # Убеждаемся, что все gaps положительные
        gaps = [g for g in gaps if g > 0]

        return gaps

    def sort_descending(self, arr):
        """
        Сортировка по убыванию
        """
        n = len(arr)
        gaps = self._get_gap_sequence(n)

        for gap in gaps:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                # Изменяем условие на противоположное
                while j >= gap and arr[j - gap] < temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp

        return arr

    def sort_with_custom_gaps(self, arr, gaps):
        """
        Сортировка с пользовательской последовательностью gap'ов
        """
        # Фильтруем gaps, оставляя только положительные и меньшие длины массива
        valid_gaps = [g for g in gaps if 0 < g < len(arr)]
        valid_gaps = sorted(set(valid_gaps), reverse=True)  # уникальные, по убыванию

        for gap in valid_gaps:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp

        return arr


# Пример использования
if __name__ == "__main__":
    print("=== СОРТИРОВКА ШЕЛЛА ===\n")

    test_array = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print(f"Исходный массив: {test_array}\n")

    # Тестируем разные последовательности
    sequences = ["shell", "hibbard", "ciura", "sedgewick", "fibonacci"]

    for seq_name in sequences:
        print(f"\nПоследовательность '{seq_name}':")
        sorter = ShellSort(gap_sequence=seq_name)

        arr = test_array.copy()
        print(f"  Было: {arr}")

        gaps = sorter._get_gap_sequence(len(arr))
        print(f"  Gaps: {gaps}")

        sorter.sort(arr)
        print(f"  Стало: {arr}")

    # Демонстрация процесса
    print("\n" + "=" * 50)
    print("ПОШАГОВАЯ ДЕМОНСТРАЦИЯ")
    print("=" * 50)

    demo = [62, 83, 18, 53, 7, 17, 95, 86, 47, 69, 25, 28]
    print(f"Исходные: {demo}")

    sorter = ShellSort(gap_sequence="shell")
    arr = demo.copy()
    n = len(arr)
    gap = n // 2

    step = 1
    while gap > 0:
        print(f"\nШаг {step}, gap = {gap}:")
        print(f"  До:    {arr}")

        for i in range(gap, n):
            temp = arr[i]
            j = i
            moved = False
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                moved = True

            if moved or j != i:
                arr[j] = temp
                print(f"    Вставляем {temp} на позицию {j}")

        print(f"  После: {arr}")
        gap //= 2
        step += 1

    print(f"\nРезультат: {arr}")

    # Демонстрация с пользовательскими gaps
    print("\n" + "=" * 50)
    print("ПОЛЬЗОВАТЕЛЬСКАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ")
    print("=" * 50)

    custom_demo = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Исходные: {custom_demo}")

    custom_gaps = [5, 3, 1]
    print(f"Пользовательские gaps: {custom_gaps}")

    sorter.sort_with_custom_gaps(custom_demo, custom_gaps)
    print(f"Результат: {custom_demo}")

    # Сравнение последовательностей
    print("\n" + "=" * 50)
    print("СРАВНЕНИЕ ПОСЛЕДОВАТЕЛЬНОСТЕЙ ДЛЯ РАЗНЫХ РАЗМЕРОВ")
    print("=" * 50)

    sizes = [10, 50, 100, 500, 1000]
    sequences_to_test = ["shell", "hibbard", "ciura", "sedgewick", "fibonacci"]

    for size in sizes:
        print(f"\nРазмер массива: {size}")
        for seq in sequences_to_test:
            sorter = ShellSort(gap_sequence=seq)
            gaps = sorter._get_gap_sequence(size)
            print(f"  {seq:10} : {gaps}")