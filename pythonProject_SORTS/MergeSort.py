class MergeSort:
    """
    СОРТИРОВКА СЛИЯНИЕМ (Merge Sort)

    Смысл: Алгоритм "разделяй и властвуй". Массив рекурсивно делится на две половины
    до тех пор, пока не останутся массивы из одного элемента, которые затем
    сливаются в отсортированном порядке.

    Преимущества:
    - Гарантированная сложность O(n log n) для любых данных
    - Стабильная сортировка (сохраняет порядок равных элементов)
    - Отлично подходит для сортировки связных списков
    - Хорошо работает с данными, которые не помещаются в память (внешняя сортировка)

    Недостатки:
    - Требует O(n) дополнительной памяти
    - Медленнее быстрой сортировки на маленьких массивах из-за накладных расходов

    Сложность: O(n log n) всегда
    Память: O(n) дополнительной памяти
    """

    def sort(self, arr):
        """
        Основной метод сортировки

        Args:
            arr: список для сортировки

        Returns:
            новый отсортированный список
        """
        # Базовый случай: массив из 0 или 1 элемента уже отсортирован
        if len(arr) <= 1:
            return arr.copy()

        # Разделяем массив на две половины
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Рекурсивно сортируем обе половины
        left_sorted = self.sort(left)
        right_sorted = self.sort(right)

        # Сливаем отсортированные половины
        return self._merge(left_sorted, right_sorted)

    def _merge(self, left, right):
        """
        Слияние двух отсортированных массивов в один отсортированный
        """
        result = []
        i = j = 0

        # Сравниваем элементы из обоих массивов и добавляем меньший
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Добавляем оставшиеся элементы из левого массива
        while i < len(left):
            result.append(left[i])
            i += 1

        # Добавляем оставшиеся элементы из правого массива
        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    def sort_in_place_version(self, arr, left=0, right=None):
        """
        Альтернативная версия, сортирующая на месте (с использованием доп. памяти)
        Больше похожа на классическую реализацию для массивов
        """
        if right is None:
            right = len(arr) - 1

        if left < right:
            mid = (left + right) // 2

            # Рекурсивно сортируем две половины
            self.sort_in_place_version(arr, left, mid)
            self.sort_in_place_version(arr, mid + 1, right)

            # Сливаем отсортированные половины
            self._merge_in_place(arr, left, mid, right)

        return arr

    def _merge_in_place(self, arr, left, mid, right):
        """
        Слияние двух отсортированных частей массива
        """
        # Создаем временные копии
        left_part = arr[left:mid + 1].copy()
        right_part = arr[mid + 1:right + 1].copy()

        i = j = 0
        k = left

        # Сливаем обратно в исходный массив
        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        # Копируем оставшиеся элементы
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
    # Тестовые данные
    test_array = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print(f"Исходный массив: {test_array}")

    # Создаем экземпляр сортировщика
    sorter = MergeSort()

    # Вариант 1: возвращает новый отсортированный массив
    sorted_array = sorter.sort(test_array)
    print(f"Сортировка (новая копия): {sorted_array}")
    print(f"Оригинал не изменился: {test_array}")

    # Вариант 2: сортировка на месте
    array_for_inplace = test_array.copy()
    sorter.sort_in_place_version(array_for_inplace)
    print(f"\nСортировка на месте: {array_for_inplace}")

    # Демонстрация стабильности
    print("\n--- Демонстрация стабильности ---")
    # Создаем список кортежей (значение, индекс_в_оригинале)
    data = [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd')]
    print(f"Исходные данные: {data}")

    # Сортируем по первому элементу (ключу)
    sorted_stable = sorted(data, key=lambda x: x[0])
    print(f"Стабильная сортировка: {sorted_stable}")
    print("(элементы с ключом 3 сохраняют исходный порядок: 'a' перед 'c')")