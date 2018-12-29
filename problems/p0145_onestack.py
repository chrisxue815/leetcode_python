import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative post-order DFS, stack.
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root

        while True:
            while curr:
                stack.append(curr)
                stack.append(curr)
                curr = curr.left

            if not stack:
                break

            curr = stack.pop()

            if stack and stack[-1] is curr:
                curr = curr.right
            else:
                result.append(curr.val)
                curr = None

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            root = TreeNode.from_array(case.root)
            actual = Solution().postorderTraversal(root)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
