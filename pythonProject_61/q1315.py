from collections import deque
from math import floor

class TreeNode:
    """Класс для узла бинарного дерева"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Значение узла
        self.left = left  # Левый потомок
        self.right = right  # Правый потомок


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """Функция вычисляет сумму всех потомков чётных дедушек"""
        self.level_order = []  # Список узлов для вывода индексов
        self.index_map = {}  # Хранение индексов узлов
        self.build_index_map(root)  # Заполняем индексы
        print("\n📌 Вывод с пояснениями для суммы:\n")
        return self.dfs(root, None, None)

    def build_index_map(self, root):
        """Формируем индексы узлов по порядку уровня"""
        queue = [(root, -1, -1)]  # (узел, индекс родителя, индекс дедушки)
        index = 0  # Текущий индекс узла

        print("📌 Вывод индексов узлов:\n")

        while queue:
            node, parent_index, grandparent_index = queue.pop(0)

            # Запоминаем индекс текущего узла
            self.index_map[node] = (index, parent_index, grandparent_index)
            self.level_order.append(node)

            # Вывод узла в нужном формате (значение, индекс родителя, индекс дедушки)
            print(f"{node.val if node else 'N'} {parent_index} {grandparent_index}")

            # Добавляем в очередь левого потомка
            if node.left:
                queue.append((node.left, index, parent_index))
            else:
                self.level_order.append(None)  # Добавляем 'N' для отсутствующего узла
                print(f"N {index} {parent_index}")

            # Добавляем в очередь правого потомка
            if node.right:
                queue.append((node.right, index, parent_index))
            else:
                self.level_order.append(None)  # Добавляем 'N' для отсутствующего узла
                print(f"N {index} {parent_index}")

            index += 1  # Переход к следующему узлу

    def dfs(self, node, parent, grandparent):
        """Рекурсивная функция обхода дерева"""
        if not node:
            return 0

        # Если дедушка существует и его значение чётное, прибавляем текущее значение
        sum_val = node.val if grandparent and grandparent.val % 2 == 0 else 0

        # Вывод пояснений
        grandparent_val = grandparent.val if grandparent else "N"
        parent_val = parent.val if parent else "N"
        print(f"Узел: {node.val}, Родитель: {parent_val}, Дедушка: {grandparent_val}, Сумма: {sum_val}")

        # Рекурсивно вызываем функцию для левого и правого потомков
        sum_val += self.dfs(node.left, node, parent)
        sum_val += self.dfs(node.right, node, parent)

        return sum_val


# Функция для создания бинарного дерева из списка значений
def buildTree(values):
    """Функция строит бинарное дерево из списка значений (уровневый порядок)"""
    if not values or values[0] == "N":
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if values[i] != "N":
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] != "N":
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def print_tree(node, level=0):
    """
    Рекурсивная функция для красивого вывода бинарного дерева в консоль.
    Отображает дерево боком, где корень - самый левый элемент,
    а правые потомки рисуются выше, левые - ниже.
    """

    if node is not None:  # Проверяем, существует ли узел (если узел пустой, ничего не делаем)

        # Рекурсивно вызываем функцию для правого поддерева, увеличивая уровень отступа
        print_tree(node.right, level=level + 1)

        # Выводим текущее значение узла с отступом, который зависит от уровня
        print(3 * ' ' * level + str(node.val))

        # Рекурсивно вызываем функцию для левого поддерева, увеличивая уровень отступа
        print_tree(node.left, level=level + 1)


if __name__ == '__main__':
    tree_repr = [50, 'N', 54, 98, 6, 'N', 'N', 'N', 34, 'N', 'N']
    root = buildTree(tree_repr)
    print_tree(root)
    print(Solution().sumEvenGrandparent(root))


    # rep5