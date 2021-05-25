import unittest

import utils
from tree import TreeNode


# O(n) time. O(n) space. Iterative pre-order DFS, bit manipulation.
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        stack = []
        index = 1
        index1 = -1

        while root or stack:
            while root:
                if root.val == x or root.val == y:
                    if index1 == -1:
                        index1 = index
                    else:
                        return index != index1 | 1 and index.bit_length() == index1.bit_length()
                index <<= 1
                stack.append((root.right, index + 1))
                root = root.left

            root, index = stack.pop()


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=utils.root_array_to_tree)


if __name__ == '__main__':
    unittest.main()
