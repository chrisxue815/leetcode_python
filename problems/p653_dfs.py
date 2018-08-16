import unittest
import utils
from tree import TreeNode


# O(nlog(n)) time. O(log(n)) space. Recursive pre-order traversal.
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def find_val(node, val, exclude):
            if not node:
                return False

            if node.val == val:
                if node is not exclude:
                    return True
                return find_val(node.left, val, exclude) or find_val(node.right, val, exclude)
            elif node.val > val:
                return find_val(node.left, val, exclude)
            else:
                return find_val(node.right, val, exclude)

        def find_complement(node):
            if not node:
                return False
            if find_val(root, k - node.val, node):
                return True
            return find_complement(node.left) or find_complement(node.right)

        return find_complement(root)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p653.json').test_cases

        for case in cases:
            root = TreeNode.from_array(case.root)
            actual = Solution().findTarget(root, case.k)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
