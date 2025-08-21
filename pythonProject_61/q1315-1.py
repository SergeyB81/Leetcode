class TreeNode:
    """Класс для узла бинарного дерева"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """Функция вычисляет сумму всех потомков чётных дедушек"""
        print("📌 Структура дерева с индексами:")
        self.print_tree_with_indices(root)
        print("\n📌 Вывод с пояснениями для суммы:")
        return self.dfs(root, None, None)

    def print_tree_with_indices(self, root):
        """Вывод дерева с индексами узлов в порядке BFS.

        Очередь хранит кортежи (node, idx, parent_idx, grandparent_idx).
        """
        if not root:
            return

        queue = [(root, 0, None, None)]
        index = 1  # следующий свободный индекс для новых узлов

        while queue:
            node, idx, parent_idx, grandparent_idx = queue.pop(0)

            parent_val = str(parent_idx) if parent_idx is not None else "N"
            grandparent_val = str(grandparent_idx) if grandparent_idx is not None else "N"
            print(f"Узел {node.val}: индекс={idx}, родитель={parent_val}, дедушка={grandparent_val}")

            if node.left:
                queue.append((node.left, index, idx, parent_idx))
                index += 1
            if node.right:
                queue.append((node.right, index, idx, parent_idx))
                index += 1

    def dfs(self, node, parent, grandparent):
        """Рекурсивная функция обхода дерева"""
        if not node:
            return 0

        sum_val = node.val if grandparent and grandparent.val % 2 == 0 else 0

        grandparent_val = grandparent.val if grandparent else "N"
        parent_val = parent.val if parent else "N"
        print(f"Узел: {node.val}, Родитель: {parent_val}, Дедушка: {grandparent_val}, Сумма: {sum_val}")

        sum_val += self.dfs(node.left, node, parent)
        sum_val += self.dfs(node.right, node, parent)

        return sum_val


def build_tree_correct(values):
    """Правильное построение дерева из списка (BFS, 'N' значит None)"""
    if not values or values[0] == "N":
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1
    n = len(values)

    while queue and i < n:
        current = queue.pop(0)

        # Левый ребенок
        if i < n and values[i] != "N":
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Правый ребенок
        if i < n and values[i] != "N":
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


def print_tree(node, level=0):
    """Рекурсивная функция для визуализации дерева"""
    if node is not None:
        print_tree(node.right, level=level + 1)
        print('   ' * level + str(node.val))
        print_tree(node.left, level=level + 1)


if __name__ == '__main__':
    # Исправленный список: 34 станет ребенком узла 98
    tree_repr = [50, 'N', 54, 98, 6, 34, 'N', 'N', 'N', 'N', 'N']

    print("📋 Исходный список:", tree_repr)
    print("🌳 Визуальное представление дерева:")

    root = build_tree_correct(tree_repr)
    print_tree(root)

    print("\n" + "="*60)

    solution = Solution()
    result = solution.sumEvenGrandparent(root)
    print(f"\n🎯 Итоговая сумма: {result}")
