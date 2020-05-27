import unittest
import utils
from tree import TreeNode


# O(n) time. O(n) space. BFS.
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = [root]

        while True:
            sum_ = 0
            new_q = []

            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
                sum_ += node.val

            if new_q:
                q = new_q
            else:
                return sum_


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().deepestLeavesSum(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
