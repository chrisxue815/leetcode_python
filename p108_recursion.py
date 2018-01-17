import unittest
from tree import TreeNode


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


class Test(unittest.TestCase):

    def test(self):
        expected = [3, 1, 5, None, 2, 4, 6]
        actual = Solution().sortedArrayToBST([1, 2, 3, 4, 5, 6]).to_array()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
