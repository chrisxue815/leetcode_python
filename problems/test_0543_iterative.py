import unittest
from typing import Optional

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative post-order DFS, stack, tree height.
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
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
                left_height = curr.left.height if curr.left else 0
                right_height = curr.right.height if curr.right else 0

                curr.height = max(left_height, right_height) + 1
                result = max(result, left_height + right_height)

                curr = None

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=TreeNode.from_root_array)


if __name__ == '__main__':
    unittest.main()
