import Queue
import unittest


def bst(nums, left, right):
    if left > right:
        return None

    index = int((left + right) / 2)
    node = TreeNode(nums[index])

    node.left = bst(nums, left, index - 1)
    node.right = bst(nums, index + 1, right)
    return node


class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return bst(nums, 0, len(nums) - 1)


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
