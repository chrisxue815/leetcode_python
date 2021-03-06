import unittest

import utils
from tree import TreeNode


# O(n) time. O(n) space. BFS.
class Solution:
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        result = 0
        q = [(root, 0)]

        while q:
            new_q = []

            for curr, num in q:
                num = (num << 1) | curr.val

                if curr.left or curr.right:
                    if curr.left:
                        new_q.append((curr.left, num))
                    if curr.right:
                        new_q.append((curr.right, num))
                else:
                    result += num

            q = new_q

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().sumRootToLeaf(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
