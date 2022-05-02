import collections
import unittest
from typing import Optional, List

import utils
from tree import TreeNode


# O(n) time. O(n) space. BFS, hash table.
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        matrix = []
        queue = [(root, 0)]
        min_col = 0
        max_col = 0

        while queue:
            new_queue = []
            row = collections.defaultdict(list)
            matrix.append(row)

            for curr, c in queue:
                row[c].append(curr.val)

                if min_col > c:
                    min_col = c
                if max_col < c:
                    max_col = c

                if curr.left:
                    new_queue.append((curr.left, c - 1))
                if curr.right:
                    new_queue.append((curr.right, c + 1))

            queue = new_queue

        result = []

        for c in range(min_col, max_col + 1):
            col = []
            result.append(col)
            for row in matrix:
                row[c].sort()
                col += row[c]

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
