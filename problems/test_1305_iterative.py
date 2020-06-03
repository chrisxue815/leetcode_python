import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative in-order DFS, merging.
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def push_left(node, stack):
            while node:
                stack.append(node)
                node = node.left

        result = []
        stack1 = []
        stack2 = []
        push_left(root1, stack1)
        push_left(root2, stack2)

        while stack1 or stack2:
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                node = stack1.pop()
                result.append(node.val)
                push_left(node.right, stack1)
            else:
                node = stack2.pop()
                result.append(node.val)
                push_left(node.right, stack2)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root1 = TreeNode.from_array(case.args.root1)
            root2 = TreeNode.from_array(case.args.root2)
            actual = Solution().getAllElements(root1, root2)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
