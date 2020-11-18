import unittest
from typing import List

import utils
from tree import TreeNode


# O(nlog(n)) time. O(log(n)) space. Recursive post-order DFS.
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        max_i, max_num = 0, nums[0]
        for i, num in enumerate(nums):
            if max_num < num:
                max_i, max_num = i, num

        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_i])
        root.right = self.constructMaximumBinaryTree(nums[max_i + 1:])

        return root


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().constructMaximumBinaryTree(**case.args.__dict__)
            actual = actual.to_array()
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
