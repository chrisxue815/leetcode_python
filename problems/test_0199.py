import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(n) space. BFS.
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        q = [root]

        while q:
            result.append(q[-1].val)
            next_q = []
            for curr in q:
                if curr.left:
                    next_q.append(curr.left)
                if curr.right:
                    next_q.append(curr.right)
            q = next_q

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
