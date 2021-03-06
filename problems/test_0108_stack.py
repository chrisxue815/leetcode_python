import unittest
from tree import TreeNode


class StackFrame:

    def __init__(self, left, right, parent, leftOrRight):
        self.left = left
        self.right = right
        self.parent = parent
        self.leftOrRight = leftOrRight


class Solution:

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        rootParent = TreeNode(0)
        stack.append(StackFrame(0, len(nums) - 1, rootParent, 'l'))

        while stack:
            frame = stack.pop()

            if frame.left <= frame.right:
                index = int((frame.left + frame.right) / 2)
                node = TreeNode(nums[index])

                if frame.leftOrRight == 'l':
                    frame.parent.left = node
                else:
                    frame.parent.right = node

                stack.append(StackFrame(index + 1, frame.right, node, 'r'))
                stack.append(StackFrame(frame.left, index - 1, node, 'l'))

        return rootParent.left


class Test(unittest.TestCase):

    def test(self):
        expected = [3, 1, 5, None, 2, 4, 6]
        actual = Solution().sortedArrayToBST([1, 2, 3, 4, 5, 6]).to_array()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
