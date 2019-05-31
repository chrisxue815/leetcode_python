import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative post-order DFS, reversed mid-right-left pre-order.
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        curr = root

        while True:
            while curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.right

            if not stack:
                break

            curr = stack.pop()
            curr = curr.left

        result.reverse()
        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().postorderTraversal(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
