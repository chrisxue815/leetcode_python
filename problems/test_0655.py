import unittest
from tree import TreeNode


def get_height(root):
    return max(get_height(root.left), get_height(root.right)) + 1 if root else 0


class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        height = get_height(root)
        result = [[] for _ in range(height)]
        que = [root]

        for rownum in range(height):
            row = result[rownum]
            side_space = (1 << (height - rownum - 1)) - 1
            mid_space = (side_space << 1) + 1
            row += [''] * side_space
            next_q = []

            for colnum, node in enumerate(que):
                if colnum:
                    row += [''] * mid_space
                if node:
                    row.append(str(node.val))
                    next_q.append(node.left)
                    next_q.append(node.right)
                else:
                    row.append('')
                    next_q.append(None)
                    next_q.append(None)

            row += [''] * side_space
            que = next_q
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [1, 2],
            [["", "1", ""],
             ["2", "", ""]]
        )
        self._test(
            [1, 2, 3, None, 4],
            [["", "", "", "1", "", "", ""],
             ["", "2", "", "", "", "3", ""],
             ["", "", "4", "", "", "", ""]]
        )
        self._test(
            [1, 2, 5, 3, None, None, None, 4],
            [["", "", "", "", "", "", "", "1", "", "", "", "", "", "", ""],
             ["", "", "", "2", "", "", "", "", "", "", "", "5", "", "", ""],
             ["", "3", "", "", "", "", "", "", "", "", "", "", "", "", ""],
             ["4", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]]
        )

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().printTree(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
