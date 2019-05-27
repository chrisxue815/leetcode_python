import unittest
from tree import TreeNode


def _find_predecessor(root):
    cur = root.left
    if not cur:
        return None
    right = cur.right
    while right and right is not root:
        cur = right
        right = cur.right
    return cur


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vals = []

        while root:
            predecessor = _find_predecessor(root)

            if not predecessor:
                vals.append(root.val)
                root = root.right
            elif predecessor.right is root:
                predecessor.right = None
                root = root.right
            else:
                vals.append(root.val)
                predecessor.right = root
                root = root.left

        return vals


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([4, 2, 6, 1, 3, 5, 7], [4, 2, 1, 3, 6, 5, 7])

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        self.assertEqual(expected, Solution().preorderTraversal(root))


if __name__ == '__main__':
    unittest.main()
