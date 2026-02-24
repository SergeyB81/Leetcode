class SelectionSort:
    """
    СОРТИРОВКА ВЫБОРОМ (Selection Sort)

    Смысл: Алгоритм делит массив на отсортированную и неотсортированную части.
    На каждом шаге находится минимальный элемент в неотсортированной части
    и меняется местами с первым элементом этой части.

    Преимущества:
    - Простая и понятная реализация
    - Минимальное количество обменов (ровно n-1)
    - Хорошо работает для маленьких массивов
    - Не требует дополнительной памяти
    - Производительность не зависит от исходного порядка данных

    Недостатки:
    - Квадратичная сложность O(n²) всегда (даже для отсортированных)
    - Нестабильная сортировка
    - Медленнее сортировки вставками на практике

    Сложность: O(n²) всегда (лучший, средний и худший случаи одинаковы)
    Память: O(1) дополнительной памяти
    """

    def sort(self, arr):
        """
        Основной метод сортировки по возрастанию

        Args:
            arr: список для сортировки

        Returns:
            отсортированный список (тот же объект)
        """
        n = len(arr)

        for i in range(n - 1):
            # Находим индекс минимального элемента в неотсортированной части
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # Меняем местами найденный минимум с текущим элементом
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]

            # Для отладки
            # print(f"  Шаг {i}: минимум {arr[i]} на позиции {i}, массив: {arr}")

        return arr

    def sort_descending(self, arr):
        """
        Сортировка по убыванию (ищем максимум вместо минимума)
        """
        n = len(arr)

        for i in range(n - 1):
            max_index = i
            for j in range(i + 1, n):
                if arr[j] > arr[max_index]:
                    max_index = j

            if max_index != i:
                arr[i], arr[max_index] = arr[max_index], arr[i]

        return arr

    def sort_with_custom_comparator(self, arr, comparator):
        """
        Сортировка с пользовательской функцией сравнения

        Args:
            arr: список для сортировки
            comparator: функция сравнения (a, b) -> True если a должен идти перед b
        """
        n = len(arr)

        for i in range(n - 1):
            best_index = i
            for j in range(i + 1, n):
                # Используем компаратор для определения порядка
                if comparator(arr[j], arr[best_index]):
                    best_index = j

            if best_index != i:
                arr[i], arr[best_index] = arr[best_index], arr[i]

        return arr

    def sort_stable_version(self, arr):
        """
        Стабильная версия сортировки выбором (но медленнее)
        Вместо обмена используем вставку со сдвигом
        """
        n = len(arr)

        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # Сохраняем минимальный элемент
            min_value = arr[min_index]

            # Сдвигаем все элементы между i и min_index вправо
            for k in range(min_index, i, -1):
                arr[k] = arr[k - 1]

