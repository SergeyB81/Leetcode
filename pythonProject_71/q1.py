from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        # Создаем список кортежей: (значение, индекс)
        # Это нужно, чтобы не потерять изначальные индексы после сортировки
        # Пример: [(2, 0), (7, 1), (11, 2), (15, 3)]
        nums_ind = [(nums[i], i) for i in range(n)]

        # Сортируем список по значениям (не по индексам!)
        # После сортировки: [(2, 0), (7, 1), (11, 2), (15, 3)]
        nums_sorted = sorted(nums_ind, key=lambda tup: tup[0])

        # Идем по отсортированному списку
        for i in range(n):
            # Вычисляем значение, которое нужно найти (target - текущее значение)
            compliment = target - nums_sorted[i][0]

            # Ищем это значение в списке через бинарный поиск
            compliment_index = self.bs(nums_sorted, 0, n - 1, compliment)

            # Если нашли и это не тот же элемент (индекс другой), то возвращаем оригинальные индексы
            if compliment_index is not None and compliment_index != i:
                return [nums_sorted[i][1], nums_sorted[compliment_index][1]]

    def bs(self, arr, start, end, target):
        # Базовый случай: один элемент остался
        if end <= start:
            if arr[start][0] == target:
                return start
            return

        # Считаем индекс середины
        mid = start + ((end - start) // 2)

        # Если нашли целевой элемент
        if target == arr[mid][0]:
            return mid
        # Если целевое значение меньше — ищем в левой части
        elif target < arr[mid][0]:
            return self.bs(arr, start, mid - 1, target)
        # Если больше — ищем в правой части
        elif target > arr[mid][0]:
            return self.bs(arr, mid + 1, end, target)

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}  # Хеш-таблица: значение -> индекс

        for i in range(n):
            # Ищем значение, которое в сумме с текущим даст target
            compliment = target - nums[i]

            # Если текущее значение уже есть в словаре — мы нашли пару
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                # Запоминаем недостающее значение (compliment) и текущий индекс
                # Пример: target = 9, nums[i] = 2 => d[7] = 0
                d[compliment] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))

#rep5++


