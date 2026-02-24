class HeapSort:
    """
    ПИРАМИДАЛЬНАЯ СОРТИРОВКА (Heap Sort)

    Смысл: Сначала строится бинарная куча (max-heap) из массива, затем
    корень (максимальный элемент) меняется с последним, размер кучи уменьшается,
    и процесс повторяется для оставшейся части.

    Преимущества:
    - Сортирует на месте (не требует дополнительной памяти)
    - Гарантированная сложность O(n log n) для любых данных
    - Хорошо подходит для систем с ограниченной памятью
    - Предсказуемое поведение (нет худшего случая как у QuickSort)

    Недостатки:
    - Нестабильная сортировка
    - На практике медленнее QuickSort из-за кэш-промахов
    - Не использует преимущества частично отсортированных данных

    Сложность: O(n log n) всегда
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

        # Шаг 1: Построение max-кучи (превращаем массив в кучу)
        # Начинаем с последнего родительского узла (n//2 - 1)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)

        # Шаг 2: Извлекаем элементы из кучи один за другим
        for i in range(n - 1, 0, -1):
            # Перемещаем текущий корень (максимум) в конец
            arr[0], arr[i] = arr[i], arr[0]

            # Восстанавливаем свойство кучи для уменьшенной кучи
            self._heapify(arr, i, 0)

        return arr

    def _heapify(self, arr, n, i):
        """
        Преобразование поддерева с корнем i в max-кучу
        (родитель >= потомков)

        Args:
            arr: массив
            n: размер кучи
            i: индекс корня поддерева
        """
        largest = i  # Инициализируем наибольший элемент как корень
        left = 2 * i + 1  # левый потомок
        right = 2 * i + 2  # правый потомок

        # Если левый потомок существует и больше корня
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Если правый потомок существует и больше текущего наибольшего
        if right < n and arr[right] > arr[largest]:
            largest = right

        # Если наибольший элемент не корень
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # меняем местами

            # Рекурсивно преобразуем затронутое поддерево
            self._heapify(arr, n, largest)

    def sort_descending(self, arr):
        """
        Сортировка по убыванию (используем min-heap вместо max-heap)
        """
        n = len(arr)

        # Строим min-кучу
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_min(arr, n, i)

        # Извлекаем элементы
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self._heapify_min(arr, i, 0)

        return arr

    def _heapify_min(self, arr, n, i):
        """Вспомогательная функция для min-кучи"""
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] < arr[smallest]:
            smallest = left

        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self._heapify_min(arr, n, smallest)


# Пример использования
if __name__ == "__main__":
    # Тестовые данные
    test_array = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print(f"Исходный массив: {test_array}")

    # Создаем экземпляр сортировщика
    sorter = HeapSort()

    # Сортируем по возрастанию
    array_asc = test_array.copy()
    sorter.sort(array_asc)
    print(f"По возрастанию: {array_asc}")

    # Сортируем по убыванию
    array_desc = test_array.copy()
    sorter.sort_descending(array_desc)
    print(f"По убыванию: {array_desc}")

    # Демонстрация построения кучи
    print("\n--- Визуализация процесса ---")
    demo_array = [4, 10, 3, 5, 1]
    print(f"Исходный массив: {demo_array}")

    # Показываем пошагово
    n = len(demo_array)
    print("Построение max-кучи:")
    for i in range(n // 2 - 1, -1, -1):
        print(f"  heapify для индекса {i} (значение {demo_array[i]})")
        sorter._heapify(demo_array, n, i)
        print(f"    результат: {demo_array}")

    print(f"\nГотовая куча: {demo_array}")
    print("Теперь извлекаем максимумы...")

    for i in range(n - 1, 0, -1):
        print(f"  Меняем корень {demo_array[0]} с элементом {demo_array[i]}")
        demo_array[0], demo_array[i] = demo_array[i], demo_array[0]
        print(f"    после обмена: {demo_array}")
        sorter._heapify(demo_array, i, 0)
        print(f"    после heapify: {demo_array}")

    print(f"Отсортированный результат: {demo_array}")