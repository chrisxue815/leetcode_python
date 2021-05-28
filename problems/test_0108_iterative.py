import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative DFS.
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        stack = []
        dummy = TreeNode(0)
        stack.append((0, len(nums), dummy, True))

        while stack:
            lo, hi, parent, is_left = stack.pop()

            if lo >= hi:
                continue

            mid = lo + ((hi - lo) >> 1)
            node = TreeNode(nums[mid])

            if is_left:
                parent.left = node
            else:
                parent.right = node

            stack.append((lo, mid, node, True))
            stack.append((mid + 1, hi, node, False))

        return dummy.left


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_result=TreeNode.to_array_inorder)


if __name__ == '__main__':
    unittest.main()
