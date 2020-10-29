import unittest
import utils
from tree import TreeNode


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        q = [root]
        level = 0

        while q:
            new_q = []
            prev_val = q[0].val + 1 if level & 1 else q[0].val - 1
            for curr in q:
                if level & 1:
                    if curr.val & 1 or prev_val <= curr.val:
                        return False
                else:
                    if curr.val & 1 == 0 or prev_val >= curr.val:
                        return False

                if curr.left:
                    new_q.append(curr.left)
                if curr.right:
                    new_q.append(curr.right)
                prev_val = curr.val

            q = new_q
            level += 1

        return True


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().isEvenOddTree(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
