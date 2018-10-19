import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative in-order DFS.
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        prev = dummy = TreeNode(0)

        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                break

            root = stack.pop()
            prev.right = root
            root.left = None
            prev = root
            root = root.right

        return dummy.right


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p897.json').test_cases

        for case in cases:
            root = TreeNode.from_array(case.root)
            actual = Solution().increasingBST(root)
            actual = actual.to_array()
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
