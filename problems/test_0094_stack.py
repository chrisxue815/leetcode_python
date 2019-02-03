import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative in-order DFS, stack.
class Solution(object):
    def inorderTraversal(self, root):
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
                curr = curr.left

            if not stack:
                break

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            root = TreeNode.from_array(case.args.root)
            actual = Solution().inorderTraversal(root)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
