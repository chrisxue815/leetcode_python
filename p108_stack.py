import Queue
import unittest


class StackFrame(object):

    def __init__(self, left, right, parent, leftOrRight):
        self.left = left
        self.right = right
        self.parent = parent
        self.leftOrRight = leftOrRight


class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        rootParent = TreeNode(0)
        stack.append(StackFrame(0, len(nums) - 1, rootParent, 'l'))

        while len(stack) > 0:
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


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def to_array(self):
        """
        Serializes binary tree in Leetcode-style using level order traversal (BFS)
        :rtype: List[int]
        """
        nodes = []
        que = Queue.Queue()
        que.put(self)

        while not que.empty():
            node = que.get()

            if node is None:
                nodes.append(None)
            else:
                nodes.append(node.val)
                que.put(node.left)
                que.put(node.right)

        while not nodes[-1]:
            nodes.pop()

        return nodes


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(Solution().sortedArrayToBST(
            [1, 2, 3, 4, 5, 6]).to_array(), [3, 1, 5, None, 2, 4, 6])


if __name__ == '__main__':
    unittest.main()
