import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative pre-order DFS, stack.
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root

        while curr or stack:
            if curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p144.json').test_cases

        for case in cases:
            root = TreeNode.from_array(case.root)
            actual = Solution().preorderTraversal(root)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
