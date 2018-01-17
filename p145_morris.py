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


def _reverse_append(root, vals):
    parent = None
    while root:
        right = root.right
        root.right = parent
        parent = root
        root = right

    root = parent
    parent = None
    while root:
        vals.append(root.val)
        right = root.right
        root.right = parent
        parent = root
        root = right


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vals = []
        dump = root

        while root:
            predecessor = _find_predecessor(root)

            if not predecessor:
                root = root.right
            elif predecessor.right is root:
                predecessor.right = None

                _reverse_append(root.left, vals)

                root = root.right
            else:
                predecessor.right = root
                root = root.left

        _reverse_append(dump, vals)

        return vals


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([4, 2, 6, 1, 3, 5, 7], [1, 3, 2, 5, 7, 6, 4])

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        self.assertEqual(expected, Solution().postorderTraversal(root))


if __name__ == '__main__':
    unittest.main()
