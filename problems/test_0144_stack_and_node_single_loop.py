import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative pre-order DFS, stack.
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        curr = root

        while curr or stack:
            if curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().preorderTraversal(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
