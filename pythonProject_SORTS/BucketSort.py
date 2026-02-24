class InsertionSort:
    """
    СОРТИРОВКА ВСТАВКАМИ (вспомогательный класс для BucketSort)

    Используется для сортировки отдельных корзин в блочной сортировке.
    """

    def sort(self, arr):
        """
        Сортировка вставками

        Args:
            arr: список для сортировки

        Returns:
            отсортированный список
        """
        n = len(arr)

        for i in range(1, n):
            key = arr[i]
            j = i - 1

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key

        return arr


class BucketSort:
    """
    БЛОЧНАЯ СОРТИРОВКА (Bucket Sort)

    Смысл: Элементы распределяются по небольшим блокам (корзинам) на основе их значения,
    затем каждый блок сортируется отдельно (обычно вставками или другой сортировкой),
    после чего блоки объединяются.

    Преимущества:
    - Линейная сложность O(n + k) при хорошем распределении
    - Отлично подходит для равномерно распределенных данных
    - Может быть стабильной при правильной реализации
    - Хорошо параллелится

    Недостатки:
    - Требует знания распределения данных
    - Производительность сильно зависит от выбора количества корзин
    - Дополнительная память O(n + k)
    - Неэффективна для неравномерно распределенных данных

    Сложность: O(n + k) в среднем, O(n²) в худшем (если все в одной корзине)
    Память: O(n + k)
    """

    def __init__(self, num_buckets=None):
        """
        Args:
            num_buckets: количество корзин (если None, вычисляется автоматически)
        """
        self.num_buckets = num_buckets

    def sort(self, arr):
        """
        Основной метод сортировки для чисел с плавающей точкой от 0 до 1

        Args:
            arr: список для сортировки (числа с плавающей точкой от 0 до 1)

        Returns:
            отсортированный список
        """
        if not arr:
            return arr

        n = len(arr)

        # Проверяем, что все числа в диапазоне [0, 1]
        if max(arr) > 1 or min(arr) < 0:
            print("  Предупреждение: числа вне диапазона [0,1], масштабируем...")
            return self.sort_general(arr)

        # Определяем количество корзин
        if self.num_buckets is None:
            self.num_buckets = int(n ** 0.5)  # квадратный корень из n
            # Минимум 2 корзины
            self.num_buckets = max(2, self.num_buckets)

        print(f"  Используем {self.num_buckets} корзин")

        # Создаем пустые корзины
        buckets = [[] for _ in range(self.num_buckets)]

        # Распределяем элементы по корзинам
        for num in arr:
            # Определяем индекс корзины для чисел от 0 до 1
            bucket_index = int(num * self.num_buckets)
            # Гарантируем, что индекс в пределах [0, num_buckets-1]
            # (для случая num = 1.0 даст индекс num_buckets)
            bucket_index = min(bucket_index, self.num_buckets - 1)
            buckets[bucket_index].append(num)

        # Сортируем каждую корзину (используем сортировку вставками для маленьких массивов)
        insertion_sorter = InsertionSort()
        for i in range(self.num_buckets):
            if buckets[i]:  # если корзина не пуста
                buckets[i] = insertion_sorter.sort(buckets[i])

        # Объединяем корзины
        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result

    def sort_general(self, arr):
        """
        Общая версия для чисел с произвольным диапазоном
        """
        if not arr:
            return arr

        n = len(arr)

        # Находим минимум и максимум
        min_val = min(arr)
        max_val = max(arr)

        # Если все числа одинаковые
        if max_val == min_val:
            return arr.copy()

        # Определяем количество корзин
        if self.num_buckets is None:
            self.num_buckets = int(n ** 0.5)
            self.num_buckets = max(2, self.num_buckets)

        print(f"  Используем {self.num_buckets} корзин")
        print(f"  Диапазон значений: [{min_val}, {max_val}]")

        # Создаем пустые корзины
        buckets = [[] for _ in range(self.num_buckets)]

        # Масштабируем и распределяем по корзинам
        range_size = max_val - min_val

        for num in arr:
            # Нормализуем в диапазон [0, 1)
            normalized = (num - min_val) / range_size
            # Определяем индекс корзины
            bucket_index = int(normalized * self.num_buckets)
            # Гарантируем, что индекс в пределах [0, num_buckets-1]
            bucket_index = min(bucket_index, self.num_buckets - 1)
            buckets[bucket_index].append(num)

        # Сортируем каждую корзину
        insertion_sorter = InsertionSort()
        for i in range(self.num_buckets):
            if buckets[i]:
                buckets[i] = insertion_sorter.sort(buckets[i])

        # Объединяем корзины
        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result

    def sort_integer_range(self, arr, min_val=None, max_val=None):
        """
        Специализированная версия для целых чисел в известном диапазоне
        """
        if not arr:
            return arr

        if min_val is None:
            min_val = min(arr)
        if max_val is None:
            max_val = max(arr)

        range_size = max_val - min_val + 1
        n = len(arr)

        # Определяем оптимальное количество корзин
        num_buckets = min(n, max(1, range_size // 10))
        num_buckets = max(2, num_buckets)

        print(f"  Используем {num_buckets} корзин для целых чисел")

        # Создаем корзины
        buckets = [[] for _ in range(num_buckets)]

        # Распределяем по корзинам
        for num in arr:
            # Линейное масштабирование в диапазон [0, num_buckets)
            normalized = (num - min_val) / range_size
            bucket_index = int(normalized * num_buckets)
            bucket_index = min(bucket_index, num_buckets - 1)
            buckets[bucket_index].append(num)

        # Сортируем и объединяем
        result = []
        for bucket in buckets:
            if bucket:
                bucket.sort()  # используем встроенную сортировку (быстрее)
                result.extend(bucket)

        return result

    def sort_floats_uniform(self, arr):
        """
        Оптимизировано для равномерно распределенных float от 0 до 1
        """
        if not arr:
            return arr

        n = len(arr)

        # Проверяем диапазон
        if max(arr) > 1 or min(arr) < 0:
            print("  Числа вне [0,1], использую общую версию")
            return self.sort_general(arr)

        # Оптимальное количество корзин ~ n
        num_buckets = min(n, 100)  # ограничиваем максимум 100 корзинами
        num_buckets = max(2, num_buckets)

        print(f"  Равномерное распределение, {num_buckets} корзин")

        buckets = [[] for _ in range(num_buckets)]

        # Распределяем
        for num in arr:
            bucket_index = int(num * num_buckets)
            bucket_index = min(bucket_index, num_buckets - 1)
            buckets[bucket_index].append(num)

        # Сортируем корзины и объединяем
        result = []
        for bucket in buckets:
            if bucket:
                bucket.sort()  # используем встроенную Timsort
                result.extend(bucket)

        return result


# Пример использования
if __name__ == "__main__":
    print("=== БЛОЧНАЯ СОРТИРОВКА ===\n")

    sorter = BucketSort()

    # 1. Равномерно распределенные числа от 0 до 1
    uniform_data = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51, 0.12, 0.92, 0.85]
    print(f"1. Равномерные [0,1]: {uniform_data}")
    result = sorter.sort_floats_uniform(uniform_data)
    print(f"   Результат: {result}")

    # 2. Целые числа в диапазоне
    integer_data = [95, 87, 62, 78, 91, 64, 81, 76, 53, 89]
    print(f"\n2. Целые числа: {integer_data}")
    result = sorter.sort_integer_range(integer_data, 50, 100)
    print(f"   Результат: {result}")

    # 3. Неравномерное распределение (исправлено)
    print(f"\n3. Неравномерное распределение:")
    skewed_data = [0.01, 0.02, 0.03, 0.98, 0.99, 0.95, 0.5]
    print(f"   Данные: {skewed_data}")
    result = sorter.sort(skewed_data)
    print(f"   Результат: {result}")

    # 4. Числа с произвольным диапазоном
    print(f"\n4. Произвольный диапазон:")
    arbitrary_data = [100, 55, 200, 75, 150, 25, 175, 125, 50, 225]
    print(f"   Данные: {arbitrary_data}")
    result = sorter.sort_general(arbitrary_data)
    print(f"   Результат: {result}")

    # 5. Демонстрация распределения по корзинам
    print("\n--- Распределение по корзинам ---")
    demo_data = [0.15, 0.22, 0.31, 0.47, 0.53, 0.68, 0.71, 0.84, 0.93]
    print(f"Данные: {demo_data}")

    # Временный сортировщик с фиксированным числом корзин
    demo_sorter = BucketSort(num_buckets=3)
    buckets = [[] for _ in range(3)]
    for num in demo_data:
        idx = int(num * 3)
        idx = min(idx, 2)
        buckets[idx].append(num)
        print(f"  {num:.2f} -> корзина {idx}")

    print(f"\nКорзины до сортировки:")
    for i, bucket in enumerate(buckets):
        print(f"  Корзина {i}: {bucket}")

    # Сортируем корзины
    insertion = InsertionSort()
    for i in range(3):
        if buckets[i]:
            buckets[i] = insertion.sort(buckets[i])

    print(f"\nКорзины после сортировки:")
    for i, bucket in enumerate(buckets):
        print(f"  Корзина {i}: {bucket}")

    # Объединяем
    result = []
    for bucket in buckets:
        result.extend(bucket)
    print(f"\nРезультат объединения: {result}")