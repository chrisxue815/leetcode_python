import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative post-order DFS, stack.
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []

        def push_left(node):
            while node:
                stack.append(node)
                stack.append(node)
                node = node.left

        push_left(root)

        while stack:
            curr = stack.pop()
            if stack and stack[-1] is curr:
                push_left(curr.right)
            else:
                result.append(curr.val)

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
