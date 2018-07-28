import unittest
from tree import TreeNode


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root

        while curr or stack:
            if curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right

        return result


class Test(unittest.TestCase):
    def test(self):
        root = TreeNode.from_array([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual([1, 2, 4, 5, 3, 6, 7], Solution().preorderTraversal(root))


if __name__ == '__main__':
    unittest.main()
