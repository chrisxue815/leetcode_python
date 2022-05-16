import unittest
from typing import List, Optional

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive DFS.
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(lo, hi):
            if lo >= hi:
                return None

            mid = lo + ((hi - lo) >> 1)
            curr = TreeNode(nums[mid])
            curr.left = dfs(lo, mid)
            curr.right = dfs(mid + 1, hi)

            return curr

        return dfs(0, len(nums))


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_result=TreeNode.to_array_inorder)


if __name__ == '__main__':
    unittest.main()
