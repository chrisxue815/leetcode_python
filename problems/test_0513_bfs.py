import unittest

import utils
from tree import TreeNode


# O(n) time. O(n) space. BFS.
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 0

        result = 0
        q = [root]

        while q:
            result = q[0].val
            new_q = []
            for curr in q:
                if curr.left:
                    new_q.append(curr.left)
                if curr.right:
                    new_q.append(curr.right)
            q = new_q

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().findBottomLeftValue(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
