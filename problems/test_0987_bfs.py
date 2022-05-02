import unittest
from typing import Optional, List

import utils
from tree import TreeNode


# O(n) time. O(n) space. BFS, hash table.
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols = {}
        queue = [(root, 0)]
        min_col = 0
        max_col = 0

        while queue:
            new_queue = []
            row = {}

            for curr, c in queue:
                cell = row.get(c, None)
                if cell is None:
                    row[c] = [curr.val]
                else:
                    cell.append(curr.val)

                if min_col > c:
                    min_col = c
                if max_col < c:
                    max_col = c

                if curr.left:
                    new_queue.append((curr.left, c - 1))
                if curr.right:
                    new_queue.append((curr.right, c + 1))

            for c, cell in row.items():
                cell.sort()
                col = cols.get(c, None)
                if col is None:
                    cols[c] = cell
                else:
                    col += cell

            queue = new_queue

        result = []
        for c in range(min_col, max_col + 1):
            result.append(cols[c])

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
