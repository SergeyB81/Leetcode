class BubbleSort:
    """
    СОРТИРОВКА ПУЗЫРЬКОМ (Bubble Sort)

    Смысл: Многократно проходит по массиву, сравнивая соседние элементы и меняя их
    местами, если они стоят в неправильном порядке. Каждый проход "выталкивает"
    наибольший элемент в конец массива (как пузырек воздуха).

    Преимущества:
    - Чрезвычайно простая реализация
    - Легко понять и объяснить
    - Хорошо для обучения основам алгоритмов
    - Может определить, что массив уже отсортирован (оптимизированная версия)
    - Стабильная сортировка

    Недостатки:
    - Очень медленная для больших массивов
    - Квадратичная сложность O(n²) даже в среднем случае
    - На практике почти никогда не используется

    Сложность: O(n²) в среднем и худшем, O(n) в лучшем (с оптимизацией)
    Память: O(1) дополнительной памяти
    """

    def sort(self, arr):
        """
        Базовая версия сортировки пузырьком

        Args:
            arr: список для сортировки

        Returns:
            отсортированный список
        """
        n = len(arr)

        # Делаем n-1 проходов
        for i in range(n - 1):
            # В каждом проходе "всплывает" максимальный элемент
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    def sort_optimized(self, arr):
        """
        Оптимизированная версия с ранним завершением

        Если за целый проход не было ни одной замены,
        массив уже отсортирован - можно завершать
        """
        n = len(arr)

        for i in range(n - 1):
            swapped = False  # флаг, были ли обмены

            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            # Если не было обменов, массив отсортирован
            if not swapped:
                break

        return arr

    def sort_descending(self, arr):
        """
        Сортировка по убыванию
        """
        n = len(arr)

        for i in range(n - 1):
            for j in range(n - 1 - i):
                if arr[j] < arr[j + 1]:  # Изменено условие
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    def sort_with_step_print(self, arr):
        """
        Демонстрационная версия с печатью каждого шага
        """
        n = len(arr)
        print(f"Исходный массив: {arr}")

        for i in range(n - 1):
            print(f"\nПроход {i + 1}:")
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    print(f"  Меняем {arr[j]} и {arr[j + 1]}", end=" -> ")
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    print(arr)
                else:
                    print(f"  {arr[j]} <= {arr[j + 1]}, не меняем")

        return arr

    def bidirectional_sort(self, arr):
        """
        Двунаправленная сортировка пузырьком (шейкерная сортировка)
        Двигается в обоих направлениях, что может быть быстрее
        """
        left = 0
        right = len(arr) - 1
        swapped = True

        while left < right and swapped:
            swapped = False

            # Движение слева направо (как обычный пузырек)
            for i in range(left, right):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            right -= 1

            # Движение справа налево
            for i in range(right, left, -1):
                if arr[i - 1] > arr[i]:
                    arr[i - 1], arr[i] = arr[i], arr[i - 1]
                    swapped = True

            left += 1

        return arr


# Пример использования
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print("=== СОРТИРОВКА ПУЗЫРЬКОМ ===\n")

    sorter = BubbleSort()

    # Базовая версия
    arr1 = test_array.copy()
    print(f"Базовая версия:")
    print(f"  Было: {arr1}")
    sorter.sort(arr1)
    print(f"  Стало: {arr1}")

    # Оптимизированная версия
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"\nОптимизированная версия на отсортированном массиве:")
    print(f"  Было: {arr2}")
    sorter.sort_optimized(arr2)
    print(f"  Стало: {arr2} (всего один проход)")

    # Демонстрация пошагово
    print("\nПошаговая демонстрация:")
    demo = [5, 1, 4, 2, 8]
    sorter.sort_with_step_print(demo.copy())

    # Шейкерная сортировка
    arr4 = test_array.copy()
    print(f"\nДвунаправленная (шейкерная) сортировка:")
    print(f"  Было: {arr4}")
    sorter.bidirectional_sort(arr4)
    print(f"  Стало: {arr4}")