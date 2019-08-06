import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(n) space. Tree BFS.
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = [root]
        left_to_right = True

        while q:
            level = []
            new_q = []

            for curr in reversed(q):
                level.append(curr.val)

                if left_to_right:
                    if curr.left:
                        new_q.append(curr.left)
                    if curr.right:
                        new_q.append(curr.right)
                else:
                    if curr.right:
                        new_q.append(curr.right)
                    if curr.left:
                        new_q.append(curr.left)

            result.append(level)
            q = new_q
            left_to_right = not left_to_right

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().zigzagLevelOrder(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
