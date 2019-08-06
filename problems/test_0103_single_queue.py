import collections
import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(n) space. Tree BFS, a single queue.
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = collections.deque([root])
        left_to_right = True

        while True:
            size = len(q)
            if size == 0:
                break

            level = []

            for _ in range(size):
                if left_to_right:
                    curr = q.popleft()
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                else:
                    curr = q.pop()
                    if curr.right:
                        q.appendleft(curr.right)
                    if curr.left:
                        q.appendleft(curr.left)

                level.append(curr.val)

            result.append(level)
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
