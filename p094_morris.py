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


class Solution(object):
    def inorderTraversal(self, root):
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
                vals.append(root.val)
                predecessor.right = None
                root = root.right
            else:
                predecessor.right = root
                root = root.left

        return vals


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([4, 2, 6, 1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7])

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        self.assertEqual(
            Solution().inorderTraversal(root),
            expected)


if __name__ == '__main__':
    unittest.main()
