import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative DFS.
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = [(root.left, root.right)]

        while q:
            left, right = q.pop()
            if left is None:
                if right is None:
                    continue
                return False
            if right is None:
                return False
            if left.val != right.val:
                return False
            q.append((left.left, right.right))
            q.append((left.right, right.left))

        return True


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=utils.root_array_to_tree)


if __name__ == '__main__':
    unittest.main()
