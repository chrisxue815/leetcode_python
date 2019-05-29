import unittest
from typing import List

from tree import TreeNode


def _find_predecessor(curr):
    p = curr.left
    if not p:
        return None
    while p.right and p.right is not curr:
        p = p.right
    return p


# O(n) time. O(1) space. Morris in-order traversal.
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        curr = root

        while curr:
            p = _find_predecessor(curr)

            if p:
                if p.right:
                    result.append(curr.val)
                    p.right = None
                    curr = curr.right
                else:
                    p.right = curr
                    curr = curr.left
            else:
                result.append(curr.val)
                curr = curr.right

        return result


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([4, 2, 6, 1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7])

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        self.assertEqual(expected, Solution().inorderTraversal(root))


if __name__ == '__main__':
    unittest.main()
