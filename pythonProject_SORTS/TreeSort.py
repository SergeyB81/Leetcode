class TreeNode:
    """Узел бинарного дерева поиска"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeSort:
    """
    СОРТИРОВКА ДЕРЕВОМ (Tree Sort)

    Смысл: Строится бинарное дерево поиска (BST) из элементов массива,
    затем выполняется симметричный обход (in-order traversal), который
    дает отсортированную последовательность.

    Преимущества:
    - Простая и элегантная концепция
    - Естественно работает с дубликатами
    - Динамическая структура (легко добавлять новые элементы)
    - Позволяет выполнять другие операции (поиск, min, max)

    Недостатки:
    - Дополнительная память O(n) для хранения дерева
    - Может выродиться в O(n²) для отсортированных данных
    - Рекурсивная реализация
    - Не сортирует на месте

    Сложность: O(n log n) в среднем, O(n²) в худшем (для вырожденного дерева)
    Память: O(n) для хранения дерева
    """

    def sort(self, arr):
        """
        Основной метод сортировки

        Args:
            arr: список для сортировки

        Returns:
            отсортированный список
        """
        if not arr:
            return []

        # Строим дерево
        root = TreeNode(arr[0])
        for value in arr[1:]:
            self._insert(root, value)

        # Обходим дерево (in-order)
        result = []
        self._inorder_traversal(root, result)

        return result

    def _insert(self, node, value):
        """
        Вставка элемента в бинарное дерево поиска
        """
        if value <= node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def _inorder_traversal(self, node, result):
        """
        Симметричный обход дерева (слева-корень-справа)
        """
        if node is None:
            return

        self._inorder_traversal(node.left, result)
        result.append(node.value)
        self._inorder_traversal(node.right, result)

    def sort_balanced(self, arr):
        """
        Версия с построением сбалансированного дерева
        Избегает вырождения для отсортированных данных
        """
        if not arr:
            return []

        # Копируем и сортируем массив
        sorted_arr = sorted(arr)  # используем встроенную сортировку

        # Строим сбалансированное дерево из отсортированного массива
        root = self._build_balanced(sorted_arr, 0, len(sorted_arr) - 1)

        # Обходим дерево
        result = []
        self._inorder_traversal(root, result)

        return result

    def _build_balanced(self, sorted_arr, start, end):
        """
        Строит сбалансированное дерево из отсортированного массива
        """
        if start > end:
            return None

        mid = (start + end) // 2
        node = TreeNode(sorted_arr[mid])

        node.left = self._build_balanced(sorted_arr, start, mid - 1)
        node.right = self._build_balanced(sorted_arr, mid + 1, end)

        return node

    def sort_with_duplicates_count(self, arr):
        """
        Версия с подсчетом дубликатов (эффективнее для многих повторений)
        """
        if not arr:
            return []

        class CountNode:
            """Узел дерева с подсчетом повторений"""

            def __init__(self, value):
                self.value = value
                self.count = 1
                self.left = None
                self.right = None

        def insert_count(node, value):
            """Вставка с подсчетом дубликатов"""
            if value == node.value:
                node.count += 1
            elif value < node.value:
                if node.left is None:
                    node.left = CountNode(value)
                else:
                    insert_count(node.left, value)
            else:
                if node.right is None:
                    node.right = CountNode(value)
                else:
                    insert_count(node.right, value)

        def inorder_count(node, result):
            """Обход с учетом количества повторений"""
            if node is None:
                return
            inorder_count(node.left, result)
            # Добавляем значение столько раз, сколько оно встречалось
            result.extend([node.value] * node.count)
            inorder_count(node.right, result)  # Исправлено: передаём result, а не node.value

        # Строим дерево
        root = CountNode(arr[0])
        for value in arr[1:]:
            insert_count(root, value)

        # Обходим
        result = []
        inorder_count(root, result)

        return result

    def visualize_tree(self, arr):
        """
        Визуализация процесса построения дерева
        """
        if not arr:
            return

        print(f"Строим дерево из: {arr}")
        root = TreeNode(arr[0])
        print(f"Корень: {arr[0]}")

        for i, value in enumerate(arr[1:], 2):
            print(f"\nВставляем {value}:")
            self._visualize_insert(root, value, "")

        print("\nСимметричный обход дерева:")
        result = []
        self._inorder_traversal(root, result)
        print(f"Результат обхода: {result}")

        return root

    def _visualize_insert(self, node, value, prefix):
        """
        Вспомогательная функция для визуализации вставки
        """
        if value <= node.value:
            if node.left is None:
                print(f"{prefix}  └── Левый потомок {node.value} -> {value}")
                node.left = TreeNode(value)
            else:
                print(f"{prefix}  ├── Идем налево от {node.value}")
                self._visualize_insert(node.left, value, prefix + "  │   ")
        else:
            if node.right is None:
                print(f"{prefix}  └── Правый потомок {node.value} -> {value}")
                node.right = TreeNode(value)
            else:
                print(f"{prefix}  ├── Идем направо от {node.value}")
                self._visualize_insert(node.right, value, prefix + "  │   ")

    def print_tree(self, root, level=0, prefix="Корень: "):
        """
        Красиво выводит дерево в консоль
        """
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.value))
            if root.left is not None or root.right is not None:
                if root.left:
                    self.print_tree(root.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if root.right:
                    self.print_tree(root.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")

    def sort_with_statistics(self, arr):
        """
        Сортировка с выводом статистики построения дерева
        """
        if not arr:
            return []

        print(f"\nПостроение дерева из {len(arr)} элементов:")

        # Счетчики для статистики
        stats = {
            'total_inserts': 0,
            'left_turns': 0,
            'right_turns': 0,
            'max_depth': 0
        }

        def insert_with_stats(node, value, depth=0):
            """Вставка со сбором статистики"""
            stats['total_inserts'] += 1
            stats['max_depth'] = max(stats['max_depth'], depth + 1)

            if value <= node.value:
                stats['left_turns'] += 1
                if node.left is None:
                    node.left = TreeNode(value)
                    print(f"  {'  ' * depth}└── Вставляем {value} слева от {node.value}")
                else:
                    print(f"  {'  ' * depth}├── Идем налево от {node.value}")
                    insert_with_stats(node.left, value, depth + 1)
            else:
                stats['right_turns'] += 1
                if node.right is None:
                    node.right = TreeNode(value)
                    print(f"  {'  ' * depth}└── Вставляем {value} справа от {node.value}")
                else:
                    print(f"  {'  ' * depth}├── Идем направо от {node.value}")
                    insert_with_stats(node.right, value, depth + 1)

        # Строим дерево
        root = TreeNode(arr[0])
        print(f"Корень: {arr[0]}")

        for value in arr[1:]:
            insert_with_stats(root, value)

        print(f"\nСтатистика построения:")
        print(f"  Всего вставок: {stats['total_inserts']}")
        print(f"  Левых поворотов: {stats['left_turns']}")
        print(f"  Правых поворотов: {stats['right_turns']}")
        print(f"  Максимальная глубина: {stats['max_depth']}")
        print(f"  Ожидаемая глубина (log2 n): {len(arr).bit_length()}")

        # Обходим дерево
        result = []
        self._inorder_traversal(root, result)

        return result


# Пример использования
if __name__ == "__main__":
    print("=== СОРТИРОВКА ДЕРЕВОМ ===\n")

    sorter = TreeSort()

    # 1. Обычная сортировка
    test_array = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print(f"1. Обычная сортировка:")
    print(f"   Было: {test_array}")
    result = sorter.sort(test_array)
    print(f"   Стало: {result}")

    # 2. Отсортированные данные (проблема вырождения)
    sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"\n2. Отсортированные данные (обычная версия):")
    print(f"   Было: {sorted_data}")
    result = sorter.sort(sorted_data)
    print(f"   Стало: {result} (дерево выродилось в список)")

    # 3. Сбалансированная версия
    print(f"\n3. Отсортированные данные (сбалансированная версия):")
    result = sorter.sort_balanced(sorted_data)
    print(f"   Стало: {result}")

    # 4. Много дубликатов (исправлено)
    duplicate_data = [5, 2, 5, 3, 5, 1, 2, 5, 3, 2]
    print(f"\n4. Много дубликатов:")
    print(f"   Было: {duplicate_data}")
    result = sorter.sort_with_duplicates_count(duplicate_data)
    print(f"   Стало: {result}")

    # 5. Визуализация процесса
    print("\n--- Визуализация построения дерева ---")
    demo = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    print(f"Данные для визуализации: {demo}")
    root = sorter.visualize_tree(demo)

    # 6. Красивый вывод дерева
    print("\n--- Структура дерева ---")
    sorter.print_tree(root)

    # 7. Сортировка со статистикой
    print("\n--- Сортировка со статистикой ---")
    random_data = [45, 22, 78, 13, 89, 34, 67, 91, 56, 23, 77, 41]
    print(f"Данные: {random_data}")
    result = sorter.sort_with_statistics(random_data)
    print(f"Результат: {result}")

    # 8. Сравнение обычной и сбалансированной версии
    print("\n--- Сравнение обычной и сбалансированной версии ---")

    # Создаем отсортированный массив
    sorted_big = list(range(1, 16))
    print(f"Отсортированный массив из 15 элементов")

    # Обычная версия
    import time

    start = time.time()
    result_normal = sorter.sort(sorted_big)
    time_normal = time.time() - start
    print(f"  Обычная версия: {time_normal:.6f} сек")

    # Сбалансированная версия
    start = time.time()
    result_balanced = sorter.sort_balanced(sorted_big)
    time_balanced = time.time() - start
    print(f"  Сбалансированная версия: {time_balanced:.6f} сек")