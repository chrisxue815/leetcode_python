import unittest
from tree import TreeNode


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if stack and stack[-1] is curr:
                    curr = curr.right
                else:
                    result.append(curr.val)
                    curr = None

        return result


class Test(unittest.TestCase):
    def test(self):
        root = TreeNode.from_array([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual([4, 5, 2, 6, 7, 3, 1], Solution().postorderTraversal(root))


if __name__ == '__main__':
    unittest.main()
