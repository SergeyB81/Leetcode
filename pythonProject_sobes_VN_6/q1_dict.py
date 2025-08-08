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
    Класс для работы с разреженными векторами (основные элементы — нули).
    Ненулевые элементы хранятся в словаре {индекс: значение}.
    """
    def __init__(self, nums: list[int]) -> None:
        self.non_zero = {}  # Словарь для ненулевых элементов
        for index, num in enumerate(nums):
            if num != 0:
                self.non_zero[index] = num  # Сохраняем только ненулевые значения


    def dot_product(self, vec: "SparseVector") -> int:
        """
        Вычисляет скалярное произведение с другим разреженным вектором.
        Алгоритм: перемножение значений по общим индексам.
        """
        result = 0
        for index in self.non_zero:
            if index in vec.non_zero:  # Если индекс есть в обоих векторах
                result += self.non_zero[index] * vec.non_zero[index]
        print(self.non_zero, vec.non_zero)

        return result

# Пример использования
nums1 = [5, 0, 1, 40, 6, 0, 8, 5, 0]  # Вектор 1
nums2 = [1, 0, 0, 2, 0, 14, 0, 0, 0]   # Вектор 2
vec1 = SparseVector(nums1)
vec2 = SparseVector(nums2)
result = vec1.dot_product(vec2)
print(result)