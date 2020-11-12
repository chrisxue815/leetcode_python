import collections
import unittest
from typing import List

import utils
from tree import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        result = []
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()

        def lookup(node):
            if not node:
                return -1

            uid = trees[node.val, lookup(node.left), lookup(node.right)]
            count[uid] += 1
            if count[uid] == 2:
                result.append(node)
            return uid

        lookup(root)
        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().findDuplicateSubtrees(root)
            actual = [root.to_array() for root in actual]
            self.assertCountEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
