import collections
import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(n) space. Recursive post-order DFS, hash table.
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        counts = collections.Counter()

        def dfs(curr):
            if not curr:
                return 0

            s = curr.val + dfs(curr.left) + dfs(curr.right)
            counts[s] += 1
            return s

        dfs(root)
        max_count = max(counts.values())
        return [s for s, count in counts.items() if count == max_count]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=utils.root_array_to_tree, check_result=self.check_result)

    def check_result(self, case, actual, msg):
        self.assertCountEqual(case.expected, actual, msg)


if __name__ == '__main__':
    unittest.main()
