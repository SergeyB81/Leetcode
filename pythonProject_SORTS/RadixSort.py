class RadixSort:
    """
    ПОРАЗРЯДНАЯ СОРТИРОВКА (Radix Sort)

    Смысл: Сортирует числа по разрядам (единицы, десятки, сотни и т.д.).
    Использует стабильную сортировку (обычно подсчетом) для каждого разряда,
    начиная с младшего (LSD) или старшего (MSD).

    Преимущества:
    - Линейная сложность O(d * (n + k)) (d - количество разрядов)
    - Стабильная сортировка
    - Отлично подходит для чисел фиксированной длины
    - Хорошо работает со строками одинаковой длины
    - Не использует сравнения

    Недостатки:
    - Требует дополнительной памяти O(n + k)
    - Эффективна только для данных с фиксированным размером ключа
    - Медленнее для данных с большим количеством разрядов
    - Не подходит для чисел с плавающей точкой (без модификации)

    Сложность: O(d * (n + k)) где d - число разрядов, k - основание системы счисления
    Память: O(n + k)
    """

    def __init__(self, base=10):
        """
        Args:
            base: основание системы счисления (обычно 10)
        """
        self.base = base

    def sort_ints(self, arr):
        """
        Сортировка целых чисел (LSD - от младшего разряда)

        Args:
            arr: список целых чисел

        Returns:
            отсортированный список
        """
        if not arr:
            return arr

        # Работаем с копией
        arr = arr.copy()

        # Находим максимальное число для определения количества разрядов
        max_val = max(arr)

        # Определяем количество разрядов
        num_digits = len(str(max_val))

        # Сортируем по каждому разряду
        for digit_pos in range(num_digits):
            arr = self._counting_sort_by_digit(arr, digit_pos)

        return arr

    def _counting_sort_by_digit(self, arr, digit_pos):
        """
        Сортировка подсчетом по указанному разряду
        """
        # Создаем корзины для каждой цифры (0-9 для base=10)
        buckets = [[] for _ in range(self.base)]

        # Распределяем числа по корзинам на основе текущего разряда
        for num in arr:
            # Получаем цифру в текущем разряде
            digit = (num // (self.base ** digit_pos)) % self.base
            buckets[digit].append(num)

        # Собираем числа обратно в порядке корзин
        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result

    def sort_ints_optimized(self, arr):
        """
        Оптимизированная версия, использующая сортировку подсчетом
        (быстрее, чем через корзины)
        """
        if not arr:
            return arr

        arr = arr.copy()

        # Находим максимальное число
        max_val = max(arr)

        # Сортируем по каждому разряду
        exp = 1  # текущий разряд: 1, 10, 100, ...
        while max_val // exp > 0:
            arr = self._counting_sort_by_digit_optimized(arr, exp)
            exp *= self.base

        return arr

    def _counting_sort_by_digit_optimized(self, arr, exp):
        """
        Оптимизированная сортировка подсчетом для одного разряда
        """
        n = len(arr)
        output = [0] * n
        count = [0] * self.base

        # Подсчет количества каждой цифры
        for i in range(n):
            digit = (arr[i] // exp) % self.base
            count[digit] += 1

        # Накопительные суммы (для стабильности)
        for i in range(1, self.base):
            count[i] += count[i - 1]

        # Заполняем результат с конца (для стабильности)
        for i in range(n - 1, -1, -1):
            digit = (arr[i] // exp) % self.base
            count[digit] -= 1
            output[count[digit]] = arr[i]

        return output

    def sort_with_negative(self, arr):
        """
        Сортировка чисел с отрицательными значениями
        Разделяем положительные и отрицательные, обрабатываем отдельно
        """
        if not arr:
            return arr

        # Разделяем на отрицательные и положительные
        negatives = [-x for x in arr if x < 0]
        positives = [x for x in arr if x >= 0]
        zeros = [0] * arr.count(0)

        # Сортируем отрицательные (в обратном порядке)
        if negatives:
            # Сортируем положительные версии отрицательных чисел
            negatives = self.sort_ints_optimized(negatives)
            # Разворачиваем и меняем знак обратно
            negatives = [-x for x in reversed(negatives)]

        # Сортируем положительные
        if positives:
            positives = self.sort_ints_optimized(positives)

        # Объединяем: отрицательные, нули, положительные
        return negatives + zeros + positives

    def sort_strings(self, strings, max_len=None):
        """
        Сортировка строк одинаковой длины
        (если разная длина - дополняем пробелами или используем MSD)
        """
        if not strings:
            return strings

        # Определяем максимальную длину
        if max_len is None:
            max_len = max(len(s) for s in strings)

        # Дополняем строки до одинаковой длины
        padded = [s.ljust(max_len) for s in strings]

        # Сортируем от последнего символа к первому (LSD для строк)
        for pos in range(max_len - 1, -1, -1):
            padded = self._counting_sort_strings(padded, pos)

        # Убираем дополнение
        return [s.strip() for s in padded]

    def _counting_sort_strings(self, strings, char_pos):
        """
        Сортировка строк по символу на указанной позиции
        """
        # Создаем корзины для всех ASCII символов (или расширяем при необходимости)
        buckets = [[] for _ in range(256)]  # ASCII

        for s in strings:
            char = s[char_pos]
            buckets[ord(char)].append(s)

        # Собираем результат
        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result

    def sort_strings_msd(self, strings):
        """
        MSD (Most Significant Digit) сортировка для строк
        Сортирует от первого символа, лучше для строк разной длины
        """
        if not strings:
            return strings

        return self._msd_sort(strings, 0)

    def _msd_sort(self, strings, depth):
        """
        Рекурсивная MSD сортировка
        """
        if len(strings) <= 1:
            return strings

        # Создаем корзины для символов
        buckets = [[] for _ in range(256)]

        # Распределяем по первому символу на текущей глубине
        for s in strings:
            if depth < len(s):
                char = s[depth]
                buckets[ord(char)].append(s)
            else:
                # Строка закончилась - идет в начало (пустые символы)
                buckets[0].append(s)

        # Рекурсивно сортируем каждую корзину (кроме пустой)
        result = []
        for i in range(256):
            if buckets[i]:
                if i > 0:  # не для "пустых" символов
                    buckets[i] = self._msd_sort(buckets[i], depth + 1)
                result.extend(buckets[i])

        return result


# Пример использования
if __name__ == "__main__":
    print("=== ПОРАЗРЯДНАЯ СОРТИРОВКА ===\n")

    sorter = RadixSort(base=10)

    # 1. Простые целые числа
    int_data = [170, 45, 75, 90, 2, 24, 802, 66]
    print(f"1. Целые числа: {int_data}")
    result = sorter.sort_ints(int_data)
    print(f"   Результат: {result}")

    # 2. Оптимизированная версия
    print(f"\n2. Оптимизированная версия:")
    result = sorter.sort_ints_optimized(int_data)
    print(f"   Результат: {result}")

    # 3. С отрицательными числами
    negative_data = [170, -45, 75, -90, 2, -24, 802, -66]
    print(f"\n3. С отрицательными: {negative_data}")
    result = sorter.sort_with_negative(negative_data)
    print(f"   Результат: {result}")

    # 4. Сортировка строк
    string_data = ["banana", "apple", "cherry", "date", "berry"]
    print(f"\n4. Строки: {string_data}")
    result = sorter.sort_strings(string_data)
    print(f"   Результат: {result}")

    # 5. Пошаговая демонстрация
    print("\n--- Пошаговая демонстрация ---")
    demo = [329, 457, 657, 839, 436, 720, 355]
    print(f"Исходные: {demo}")

    arr = demo.copy()
    max_val = max(arr)
    exp = 1
    step = 1

    while max_val // exp > 0:
        print(f"\nШаг {step} (разряд {exp}):")

        # Показываем цифры в текущем разряде
        digits = [(num // exp) % 10 for num in arr]
        print(f"  Цифры: {digits}")

        # Сортируем
        arr = sorter._counting_sort_by_digit_optimized(arr, exp)
        print(f"  После: {arr}")

        exp *= 10
        step += 1

    # 6. Сравнение LSD и MSD для строк
    print("\n--- LSD vs MSD для строк ---")
    words = ["cat", "car", "bat", "bar", "can", "ball", "catapult"]
    print(f"Исходные: {words}")

    lsd_sorted = sorter.sort_strings(words)
    print(f"LSD сортировка: {lsd_sorted}")

    msd_sorted = sorter.sort_strings_msd(words)
    print(f"MSD сортировка: {msd_sorted}")