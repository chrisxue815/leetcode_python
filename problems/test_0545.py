import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. pre-order, in-order, and post-order DFS.
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        result = []

        def dfs(curr, is_root, leftmost, rightmost):
            if not curr:
                return

            appended = False

            if leftmost:
                result.append(curr.val)
                appended = True

            if curr.left:
                dfs(curr.left, False, leftmost, rightmost and not is_root and not curr.right)

            if not appended and not curr.left and not curr.right:
                result.append(curr.val)
                appended = True

            if curr.right:
                dfs(curr.right, False, leftmost and not is_root and not curr.left, rightmost)

            if not appended and rightmost:
                result.append(curr.val)

        dfs(root, True, True, True)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().boundaryOfBinaryTree(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
