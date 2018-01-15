import unittest
from tree import TreeNode


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        result = []
        q = [root]

        while q:
            sum_ = 0
            next_q = []
            for node in q:
                sum_ += node.val
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            result.append(float(sum_) / len(q))
            q = next_q

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [3, 9, 20, None, None, 15, 7],
            [3, 14.5, 11])

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().averageOfLevels(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
