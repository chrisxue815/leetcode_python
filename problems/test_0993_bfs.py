import collections
import unittest

import utils
from tree import TreeNode


# O(n) time. O(n) space. BFS, bit manipulation.
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = collections.deque()
        q.append(root)

        while q:
            j = -1

            for i in range(len(q)):
                curr = q.popleft()
                if not curr:
                    continue

                if curr.val == x or curr.val == y:
                    if j == -1:
                        j = i
                    else:
                        return i != j | 1

                q.append(curr.left)
                q.append(curr.right)

            if j != -1:
                return False


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=utils.root_array_to_tree)


if __name__ == '__main__':
    unittest.main()
