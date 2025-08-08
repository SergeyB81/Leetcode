"""
Задача: Реализовать класс SparseVector для эффективной работы с разреженными векторами (векторы с большим количеством нулей).

Требования:
1. Конструктор принимает список чисел, сохраняя только ненулевые элементы
2. Реализовать метод dot_product() для вычисления скалярного произведения
3. Оптимизировать хранение и вычисления для работы с разреженными данными

Пример использования:
nums1 = [5, 0, 1, 40, 6, 0, 8, 5, 0]
nums2 = [1, 0, 0, 2, 0, 14, 0, 0, 0]
vec1 = SparseVector(nums1)
vec2 = SparseVector(nums2)
result = vec1.dot_product(vec2)
"""

class SparseVector:
    """
    Класс для работы с разреженными векторами.
    Ненулевые элементы хранятся как список кортежей (индекс, значение).
    """
    def __init__(self, nums: list[int]) -> None:
        self.elements = []  # Список кортежей (индекс, значение)
        for index, num in enumerate(nums):
            if num != 0:
                self.elements.append((index, num))  # Добавляем только ненулевые

    def dot_product(self, vec: "SparseVector") -> int:
        """
        Вычисляет скалярное произведение через метод двух указателей.
        Эффективно для упорядоченных списков.
        """
        result = 0
        i = j = 0  # Указатели для обхода self.elements и vec.elements
        while i < len(self.elements) and j < len(vec.elements):
            idx1, val1 = self.elements[i]  # Текущий элемент первого вектора
            idx2, val2 = vec.elements[j]   # Текущий элемент второго вектора
            if idx1 == idx2:                # Совпадающие индексы
                result += val1 * val2
                i += 1
                j += 1
            elif idx1 < idx2:               # Увеличиваем указатель первого вектора
                i += 1
            else:                           # Увеличиваем указатель второго вектора
                j += 1
        return result

# Пример использования
nums1 = [5, 0, 1, 40, 6, 0, 8, 5, 0]  # Вектор 1
nums2 = [1, 0, 0, 2, 0, 14, 0, 0, 0]   # Вектор 2
vec1 = SparseVector(nums1)
vec2 = SparseVector(nums2)
result = vec1.dot_product(vec2)
print(result)