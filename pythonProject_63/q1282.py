from typing import List
from collections import OrderedDict
from collections import defaultdict

# Класс с методом для группировки людей по размерам групп
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Получаем уникальные значения размеров групп и сортируем их
        groups = sorted(list(set(groupSizes)))

        # Создаём упорядоченный словарь, чтобы сохранить порядок добавления ключей
        group_dict = OrderedDict()
        for group in groups:
            # Если размер группы уже есть в словаре, ничего не делаем
            if group in group_dict:
                pass
            else:
                # Иначе добавляем ключ и пустой список
                group_dict[group] = []

        # Заполняем словарь: ключ — размер группы, значение — список индексов людей
        for i, gs in enumerate(groupSizes):
            group_dict[gs].append(i)

        # Это итоговый список всех сформированных групп
        list_of_groups = []

        # Обрабатываем каждый элемент словаря
        for gs, elements in group_dict.items():
            n = len(elements)  # Общее количество людей с таким размером группы
            l = []  # Временный список для одной группы
            i = 0   # Индекс по массиву elements
            while i < n:
                if len(l) < gs:
                    # Пока в группе меньше людей, чем положено, добавляем
                    l.append(elements[i])
                else:
                    # Если группа заполнена — добавляем её в итоговый список
                    list_of_groups.append(l)
                    i = i - 1  # Возвращаемся на шаг назад, чтобы не потерять элемент
                    l = []     # Очищаем временный список для следующей группы
                i = i + 1

            # Добавляем последнюю неполную (но по размеру верную) группу
            list_of_groups.append(l)

        # Возвращаем все сформированные группы
        return list_of_groups

    def groupThePeople1(self, groupSizes: List[int]) -> List[List[int]]:
        size_to_people = defaultdict(list)  # Словарь: ключ — размер группы, значение — индексы людей
        result = []  # Итоговый список групп

        for i, size in enumerate(groupSizes):
            size_to_people[size].append(i)  # Добавляем человека в соответствующий список
            # Если набралось достаточно людей для полной группы — формируем группу
            if len(size_to_people[size]) == size:
                result.append(size_to_people[size])
                size_to_people[size] = []  # Очищаем временный список для следующей группы

        return result

# Проверка работы функции
if __name__ == '__main__':
    groupSizes = [3, 3, 3, 3, 3, 1, 3]
    print(Solution().groupThePeople1(groupSizes))