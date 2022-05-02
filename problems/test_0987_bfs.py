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

        while queue:
            new_queue = []
            row = {}

            for curr, c in queue:
                cell = row.get(c, None)
                if cell is None:
                    row[c] = [curr.val]
                else:
                    cell.append(curr.val)

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
        for c, col in sorted(cols.items()):
            result.append(col)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
