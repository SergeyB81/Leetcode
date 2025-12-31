class Solution:

    def _gey_max_depth(self, root):
        global max_depth
        max_depth = 0

        def _get_max_depth(node, level):
            global max_depth
            if node is not None:
                _get_max_depth(node.right, level=level + 1)
                if level > max_depth:
                    max_depth = level

            _get_max_depth(node.left, level=level + 1)

        _get_max_depth(root)
        return max_depth




