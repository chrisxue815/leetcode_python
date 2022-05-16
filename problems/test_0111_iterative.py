import collections
import unittest
from typing import Optional

import utils
from tree import TreeNode


# O(n) time. O(n) space. BFS.
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = collections.deque()
        q.append(root)
        depth = 1

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr.left and not curr.right:
                    return depth
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            depth += 1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
