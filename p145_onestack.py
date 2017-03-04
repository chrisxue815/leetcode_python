import unittest
from tree import TreeNode


def peek(stack):
    if stack:
        return stack[-1]
    else:
        return None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        vals = []
        stack = []
        cur = root

        while True:
            while cur:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if cur.right and cur.right == peek(stack):
                stack.pop()
                stack.append(cur)
                cur = cur.right
            else:
                vals.append(cur.val)
                cur = None
                if not stack:
                    break

        return vals


class Test(unittest.TestCase):
    def test(self):
        root = TreeNode.from_array([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(
            Solution().postorderTraversal(root),
            [4, 5, 2, 6, 7, 3, 1])


if __name__ == '__main__':
    unittest.main()
