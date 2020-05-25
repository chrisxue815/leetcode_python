import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Stack.
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]

        for i in range(1, len(preorder)):
            val = preorder[i]
            node = TreeNode(val)

            if val < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
            else:
                parent = stack.pop()
                while stack and stack[-1].val < val:
                    parent = stack.pop()
                parent.right = node
                stack.append(node)

        return root


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().bstFromPreorder(case.args.preorder)
            actual = TreeNode.to_array(actual)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
