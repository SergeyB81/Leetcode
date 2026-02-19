from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


# geeks for geeks
def buildTree(ip):
    # Create the root of the tree
    root = TreeNode(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = TreeNode(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = TreeNode(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level=level + 1)
        print(3 * ' ' * level + str(node.val))
        print_tree(node.left, level=level + 1)

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        # Этот список будет содержать все узлы дерева в порядке возрастания значений
        self.inorder = []

        # Вспомогательная функция для симметричного обхода дерева (inorder)
        # Обход: левый -> корень -> правый
        def _inorder_traversal(node):
            if node is not None:
                _inorder_traversal(node.left)
                self.inorder.append(node)  # Добавляем узел в список
                _inorder_traversal(node.right)

        # Запускаем обход от корня
        _inorder_traversal(root)

        # Количество узлов
        n = len(self.inorder)

        # Создаём массив накопленных сумм справа налево
        # Пример: если узлы [1, 2, 5] → cumsum = [8, 7, 5]
        cumsum = [0] * n  # Инициализируем массив нулями
        cumsum[-1] = self.inorder[-1].val  # Последний узел — он сам себе сумма

        # Идём справа налево и накапливаем суммы
        for i in range(n - 2, -1, -1):
            cumsum[i] = self.inorder[i].val + cumsum[i + 1]

        # Обновляем значения узлов в порядке возрастания
        for i in range(n):
            self.inorder[i].val = cumsum[i]

        # Возвращаем изменённое дерево
        return root

if __name__ == '__main__':
    root_arr = [4, 1, 6, 0, 2, 5, 7, 'N', 'N', 'N', 3, 'N', 'N', 'N', 8]
    root = buildTree(root_arr)
    print_tree(root)
    print(Solution().bstToGst(root))
    print_tree(root)

    #rep5+
