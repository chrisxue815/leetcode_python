import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative in-order DFS, merging.
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def advance(node, stack):
            while node:
                stack.append(node)
                node = node.left
            if stack:
                return stack.pop()
            else:
                return None

        result = []
        stack1 = []
        stack2 = []
        node1 = advance(root1, stack1)
        node2 = advance(root2, stack2)

        while node1 and node2:
            if node1.val <= node2.val:
                result.append(node1.val)
                node1 = advance(node1.right, stack1)
            else:
                result.append(node2.val)
                node2 = advance(node2.right, stack2)

        if not node1:
            node1 = node2
            stack1 = stack2

        while node1:
            result.append(node1.val)
            node1 = advance(node1.right, stack1)

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
