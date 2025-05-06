from typing import List
from collections import OrderedDict
from collections import defaultdict

# Класс с решением задачи
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Получаем уникальные размеры групп и сортируем их
        groups = sorted(list(set(groupSizes)))

        # Используем OrderedDict для сохранения порядка вставки
        group_dict = OrderedDict()
        for group in groups:
            # Если такого ключа ещё нет — создаём пустой список
            if group not in group_dict:
                group_dict[group] = []

        # Заполняем словарь: каждому размеру группы соответствуют индексы людей
        for i, gs in enumerate(groupSizes):
            group_dict[gs].append(i)

        # Здесь мы будем хранить финальные группы
        list_of_groups = []

        # Проходим по каждой записи в словаре
        for gs, elements in group_dict.items():
            n = len(elements)  # сколько человек с таким размером группы
            l = []             # временный список для одной группы
            i = 0              # счётчик
            while i < n:
                if len(l) < gs:      # если текущая группа не достигла нужного размера
                    l.append(elements[i])
                else:
                    list_of_groups.append(l)  # добавляем собранную группу
                    i -= 1                    # возвращаемся на текущий элемент, т.к. он не вошёл в предыдущую группу
                    l = []                    # начинаем новую группу
                i += 1

            # добавляем последнюю группу (если она не пуста)
            list_of_groups.append(l)

        return list_of_groups


class Solution:
    def groupThePeople1(self, groupSizes: List[int]) -> List[List[int]]:
        size_to_people = defaultdict(list) # defaultdict автоматически создаёт для него значение по умолчанию
                                           # (в данном случае — пустой список).
        result = []

        # Группируем людей по нужному размеру группы
        for person_id, group_size in enumerate(groupSizes):
            size_to_people[group_size].append(person_id)

        # Разбиваем по подгруппам нужного размера
        for group_size, people in size_to_people.items():
            for i in range(0, len(people), group_size):
                result.append(people[i:i + group_size])

        return result




if __name__ == '__main__':
    groupSizes = [3, 3, 3, 3, 3, 1, 3,3]
    print(Solution().groupThePeople1(groupSizes))

    #rep2
