import unittest
import utils
from tree import TreeNode

# O(n) time. O(n) space. BFS.
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        q = [(root, None)]

        while q:
            new_q = []
            found_parent = None

            for i, (curr, parent) in enumerate(q):
                if not curr:
                    continue

                if curr.val == x or curr.val == y:
                    if found_parent:
                        return found_parent is not parent
                    else:
                        found_parent = parent

                new_q.append((curr.left, curr))
                new_q.append((curr.right, curr))

            if found_parent:
                return False

            q = new_q


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p993.json').test_cases

        for case in cases:
            root = TreeNode.from_array(case.root)
            actual = Solution().isCousins(root, case.x, case.y)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
