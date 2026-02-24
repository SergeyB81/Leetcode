"""
СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ВСЕХ АЛГОРИТМОВ СОРТИРОВКИ
Упрощённая версия без matplotlib (только консольный вывод)
"""

import time
import random
from collections import defaultdict
import sys
import os

# Добавляем путь к папке с сортировками
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Импортируем все классы сортировок
from QuickSort import QuickSort
from MergeSort import MergeSort
from HeapSort import HeapSort
from TimSort import TimSort
from InsertionSort import InsertionSort
from SelectionSort import SelectionSort
from BubbleSort import BubbleSort
from BucketSort import BucketSort
from CountingSort import CountingSort
from RadixSort import RadixSort
from ShellSort import ShellSort
from TreeSort import TreeSort


class SortingBenchmark:
    """
    Класс для сравнения производительности всех алгоритмов сортировки
    """

    def __init__(self):
        self.sorters = {
            "QuickSort": QuickSort(),
            "MergeSort": MergeSort(),
            "HeapSort": HeapSort(),
            "Timsort": TimSort(),
            "InsertionSort": InsertionSort(),
            "SelectionSort": SelectionSort(),
            "BubbleSort": BubbleSort(),
            "BucketSort": BucketSort(),
            "CountingSort": CountingSort(),
            "RadixSort": RadixSort(),
            "ShellSort": ShellSort(),
            "TreeSort": TreeSort(),
        }

        # Исключаем очень медленные для больших массивов
        self.fast_sorters = {
            "QuickSort": QuickSort(),
            "MergeSort": MergeSort(),
            "HeapSort": HeapSort(),
            "Timsort": TimSort(),
            "RadixSort": RadixSort(),
            "ShellSort": ShellSort(),
            "CountingSort": CountingSort(),
            "BucketSort": BucketSort(),
        }

    def generate_data(self, size, data_type="random"):
        """
        Генерирует тестовые данные
        """
        if data_type == "random":
            return [random.randint(0, 1000) for _ in range(size)]
        elif data_type == "sorted":
            return list(range(size))
        elif data_type == "reversed":
            return list(range(size, 0, -1))
        elif data_type == "nearly_sorted":
            arr = list(range(size))
            # Меняем местами несколько пар (примерно 5% элементов)
            swaps = max(1, size // 20)
            for _ in range(swaps):
                i, j = random.sample(range(size), 2)
                arr[i], arr[j] = arr[j], arr[i]
            return arr
        elif data_type == "few_unique":
            return [random.randint(0, 10) for _ in range(size)]
        elif data_type == "floats":
            return [random.random() for _ in range(size)]
        elif data_type == "small_range":
            return [random.randint(0, 100) for _ in range(size)]

    def benchmark_single(self, sorter_name, sorter, arr, data_desc):
        """
        Тестирует одну сортировку
        """
        try:
            arr_copy = arr.copy()

            # Засекаем время
            start = time.time()

            # Вызываем соответствующий метод сортировки
            if sorter_name == "MergeSort":
                # MergeSort возвращает новую копию
                result = sorter.sort(arr_copy)
            elif sorter_name == "BucketSort":
                if data_desc == "floats" or (max(arr) <= 1 and min(arr) >= 0):
                    result = sorter.sort_floats_uniform(arr_copy)
                else:
                    result = sorter.sort_general(arr_copy)
            elif sorter_name == "CountingSort":
                # CountingSort требует неотрицательные числа
                if min(arr_copy) >= 0:
                    result = sorter.sort_with_negative(arr_copy)
                else:
                    # Для отрицательных используем специальную версию
                    result = sorter.sort_with_negative(arr_copy)
            elif sorter_name == "RadixSort":
                if min(arr_copy) < 0:
                    result = sorter.sort_with_negative(arr_copy)
                else:
                    result = sorter.sort_ints_optimized(arr_copy)
            elif sorter_name == "TreeSort":
                result = sorter.sort(arr_copy)
            else:
                # Большинство сортируют на месте
                result = sorter.sort(arr_copy)

            elapsed = time.time() - start

            # Проверяем корректность (только для отладки, можно отключить для скорости)
            # if result != sorted(arr):
            #     print(f"  Ошибка сортировки в {sorter_name}!")
            #     return None

            return elapsed

        except Exception as e:
            print(f"  Ошибка в {sorter_name}: {e}")
            return None

    def run_benchmark(self, sizes=None, data_types=None):
        """
        Запускает полное сравнение
        """
        if sizes is None:
            sizes = [100, 500, 1000, 5000]

        if data_types is None:
            data_types = ["random", "sorted", "reversed", "nearly_sorted", "few_unique", "floats"]

        results = defaultdict(lambda: defaultdict(list))

        # Заголовок
        print("\n" + "=" * 100)
        print(" " * 35 + "СРАВНЕНИЕ АЛГОРИТМОВ СОРТИРОВКИ")
        print("=" * 100)

        for size in sizes:
            print(f"\n{'=' * 50}")
            print(f" РАЗМЕР МАССИВА: {size}")
            print(f"{'=' * 50}")

            for data_type in data_types:
                print(f"\n--- Тип данных: {data_type.upper()} ---")

                # Генерируем данные
                arr = self.generate_data(size, data_type)

                # Выбираем сортировщики в зависимости от размера
                if size > 1000 and data_type not in ["few_unique", "small_range"]:
                    sorters_to_test = self.fast_sorters
                else:
                    sorters_to_test = self.sorters

                # Таблица результатов
                print(f"\n{'Алгоритм':<20} {'Время (сек)':<15} {'Статус':<10}")
                print("-" * 50)

                for name, sorter in sorters_to_test.items():
                    # Пропускаем очень медленные для больших размеров
                    if size > 500 and name in ["BubbleSort", "InsertionSort", "SelectionSort"]:
                        print(f"{name:<20} {'-':<15} {'пропущен':<10}")
                        continue

                    elapsed = self.benchmark_single(name, sorter, arr, data_type)
                    if elapsed is not None:
                        results[name][f"{data_type}_{size}"].append(elapsed)

                        # Цветной вывод для быстрых/медленных
                        if elapsed < 0.001:
                            status = "⚡ быстрый"
                        elif elapsed < 0.01:
                            status = "✓ ок"
                        elif elapsed < 0.1:
                            status = "⋯ средний"
                        else:
                            status = "⚠ медленный"

                        print(f"{name:<20} {elapsed:<15.6f} {status:<10}")

        return results

    def print_summary(self, results, sizes):
        """
        Выводит сводную таблицу результатов
        """
        print("\n" + "=" * 100)
        print(" " * 40 + "СВОДНАЯ ТАБЛИЦА")
        print("=" * 100)

        data_types = ["random", "sorted", "reversed", "nearly_sorted"]
        titles = ["Случайные", "Отсортированные", "Обратный порядок", "Почти отсортированные"]

        for data_type, title in zip(data_types, titles):
            print(f"\n--- {title} данные ---")
            print(f"{'Алгоритм':<20} ", end="")
            for size in sizes:
                print(f"{size:>12}", end="")
            print()
            print("-" * (20 + 15 * len(sizes)))

            # Собираем все алгоритмы
            all_sorters = sorted(results.keys())

            for sorter in all_sorters:
                print(f"{sorter:<20}", end="")
                for size in sizes:
                    key = f"{data_type}_{size}"
                    if key in results[sorter] and results[sorter][key]:
                        time_val = results[sorter][key][0]
                        print(f"{time_val:12.6f}", end="")
                    else:
                        print(f"{'':>12}", end="")
                print()

    def find_fastest(self, results, size=1000, data_type="random"):
        """
        Находит самый быстрый алгоритм для заданных условий
        """
        key = f"{data_type}_{size}"
        times = {}

        for sorter in results:
            if key in results[sorter] and results[sorter][key]:
                times[sorter] = results[sorter][key][0]

        if not times:
            print(f"Нет данных для {data_type} размер {size}")
            return

        # Сортируем по времени
        sorted_times = sorted(times.items(), key=lambda x: x[1])

        print(f"\n{'=' * 60}")
        print(f" ТОП-5 АЛГОРИТМОВ ДЛЯ {data_type.upper()} ДАННЫХ (размер {size})")
        print(f"{'=' * 60}")
        print(f"{'Место':<8} {'Алгоритм':<20} {'Время (сек)':<15} {'Отн. скорость':<15}")
        print("-" * 60)

        base_time = sorted_times[0][1]
        for i, (name, time_val) in enumerate(sorted_times[:5], 1):
            rel_speed = base_time / time_val if time_val > 0 else 0
            medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f"{i}.")
            print(f"{medal:<8} {name:<20} {time_val:<15.6f} {rel_speed:<15.2f}x")


# Пример использования
if __name__ == "__main__":
    print("=" * 100)
    print(" " * 35 + "ТЕСТИРОВАНИЕ АЛГОРИТМОВ СОРТИРОВКИ")
    print("=" * 100)

    benchmark = SortingBenchmark()

    # Запускаем тесты для разных размеров
    sizes = [100, 500, 1000]  # Можно добавить 5000, но будет долго
    results = benchmark.run_benchmark(sizes=sizes)

    # Выводим сводную таблицу
    benchmark.print_summary(results, sizes)

    # Находим лучшие алгоритмы для разных случаев
    benchmark.find_fastest(results, size=1000, data_type="random")
    benchmark.find_fastest(results, size=1000, data_type="sorted")
    benchmark.find_fastest(results, size=1000, data_type="few_unique")

    print("\n" + "=" * 100)
    print(" " * 30 + "РЕКОМЕНДАЦИИ ПО ВЫБОРУ АЛГОРИТМА")
    print("=" * 100)
    print("""
    📊 УНИВЕРСАЛЬНОЕ РЕШЕНИЕ:
        • Timsort - используется в Python, отлично работает на реальных данных

    🚀 ДЛЯ БОЛЬШИХ ДАННЫХ:
        • QuickSort - быстро на случайных данных
        • MergeSort - гарантированная скорость, стабильность

    💾 ПРИ ОГРАНИЧЕННОЙ ПАМЯТИ:
        • HeapSort - сортирует на месте, гарантированная сложность

    🎯 СПЕЦИАЛИЗИРОВАННЫЕ СЛУЧАИ:
        • CountingSort - для целых чисел в узком диапазоне
        • RadixSort - для многоразрядных чисел
        • BucketSort - для равномерно распределенных данных
        • InsertionSort - для маленьких массивов (< 50 элементов)

    📚 ДЛЯ ОБУЧЕНИЯ:
        • BubbleSort - простой для понимания
        • SelectionSort - наглядно показывает идею выбора
    """)