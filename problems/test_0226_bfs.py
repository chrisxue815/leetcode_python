import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. BFS.
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        q = [root]

        while q:
            new_q = []
            for curr in q:
                curr.left, curr.right = curr.right, curr.left
                if curr.left:
                    new_q.append(curr.left)
                if curr.right:
                    new_q.append(curr.right)
            q = new_q

        return root


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().invertTree(root)
            actual = TreeNode.to_array(actual)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
