from collections import deque  # Импорт очереди с двумя концами для построения дерева

# Класс, представляющий узел бинарного дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # Значение узла
        self.left = left        # Левый потомок
        self.right = right      # Правый потомок

    def __repr__(self):
        return str(self.val)    # Упрощенное представление узла при печати


# Класс, содержащий методы решения задачи
class Solution:

    # Метод для определения максимальной глубины дерева
    def get_max_depth(self, root):
        global max_depth        # Используем глобальную переменную для хранения максимальной глубины
        max_depth = 0

        # Вспомогательная рекурсивная функция
        def _get_max_depth(node, level=0):
            global max_depth
            if node is not None:
                # Сначала обходим правое поддерево
                _get_max_depth(node.right, level=level + 1)

                # Обновляем максимальную глубину, если текущий уровень больше
                if level > max_depth:
                    max_depth = level

                # Затем обходим левое поддерево
                _get_max_depth(node.left, level=level + 1)

        # Запускаем рекурсивный обход с корня
        _get_max_depth(root)
        return max_depth

    # Метод для нахождения суммы значений всех самых глубоких листьев
    def deepestLeavesSum(self, root: TreeNode) -> int:
        global max_depth        # Максимальная глубина дерева
        global sum_max_depth    # Сумма значений на максимальной глубине

        max_depth = self.get_max_depth(root)  # Сначала находим максимальную глубину
        sum_max_depth = 0

        # Вспомогательная рекурсивная функция обхода дерева
        def _traverse(node, level=0):
            global max_depth
            global sum_max_depth

            if node is not None:
                # Обходим правое поддерево
                _traverse(node.right, level=level + 1)

                # Если мы на максимальной глубине, добавляем значение узла к сумме
                if level == max_depth:
                    sum_max_depth = sum_max_depth + node.val

                # Обходим левое поддерево
                _traverse(node.left, level=level + 1)

        # Запускаем обход дерева с корня
        _traverse(root)
        return sum_max_depth


# Функция построения бинарного дерева из списка строк (значений узлов)
def buildTree(ip):
    # Создаем корень дерева
    root = TreeNode(int(ip[0]))
    size = 0  # Отслеживаем количество узлов в очереди
    q = deque()  # Очередь для построения дерева

    # Добавляем корень в очередь
    q.append(root)
    size = size + 1

    # Начинаем с элемента под индексом 1
    i = 1
    while (size > 0 and i < len(ip)):
        # Получаем текущий узел из очереди
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Получаем значение для левого потомка
        currVal = ip[i]

        # Если левый потомок не "N" (не None)
        if (currVal != "N"):
            currNode.left = TreeNode(int(currVal))  # Создаем левый узел
            q.append(currNode.left)  # Добавляем в очередь
            size = size + 1

        i = i + 1
        if (i >= len(ip)):
            break

        # Получаем значение для правого потомка
        currVal = ip[i]
        if (currVal != "N"):
            currNode.right = TreeNode(int(currVal))  # Создаем правый узел
            q.append(currNode.right)  # Добавляем в очередь
            size = size + 1

        i = i + 1

    return root


# Функция печати дерева (для наглядности)
def print_tree(node, level=0):
    if node is not None:
        # Печатаем правое поддерево (с отступом)
        print_tree(node.right, level=level + 1)

        # Печатаем текущий узел с отступом по уровню
        print(3 * ' ' * level + str(node.val))

        # Печатаем левое поддерево
        print_tree(node.left, level=level + 1)

if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, 'N', 6, 7, 'N', 'N', 'N', 'N', 8]
    nodes = [6, 7, 8, 2, 7, 1, 3, 9, 'N', 1, 4, 'N', 'N', 'N', 5]
    root = buildTree(nodes)
    print(root)

    print_tree(root)

    print(Solution().get_max_depth(root))
    print(Solution().deepestLeavesSum(root))
    # look it more 2

