import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(n) space. Recursive in-order DFS, merging.
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(curr, values):
            if not curr:
                return
            dfs(curr.left, values)
            values.append(curr.val)
            dfs(curr.right, values)

        v1 = []
        v2 = []
        dfs(root1, v1)
        dfs(root2, v2)

        result = [0] * (len(v1) + len(v2))
        i1 = i2 = 0
        for i in range(len(result)):
            if i2 >= len(v2) or i1 < len(v1) and v1[i1] < v2[i2]:
                result[i] = v1[i1]
                i1 += 1
            else:
                result[i] = v2[i2]
                i2 += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root1 = TreeNode.from_array(case.args.root1)
            root2 = TreeNode.from_array(case.args.root2)
            actual = Solution().getAllElements(root1, root2)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
