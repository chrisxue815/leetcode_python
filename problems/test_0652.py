import collections
import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(n) space. Recursive post-order DFS, hash table.
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        result = []
        uids = collections.defaultdict()
        uids.default_factory = uids.__len__
        count = collections.Counter()

        def lookup(node):
            if not node:
                return -1

            uid = uids[node.val, lookup(node.left), lookup(node.right)]
            count[uid] += 1
            if count[uid] == 2:
                result.append(node)
            return uid

        lookup(root)
        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution,
                   process_args=TreeNode.from_root_array,
                   process_result=self.process_result,
                   check_result=self.check_result)

    @staticmethod
    def process_result(actual):
        return [root.to_array() for root in actual]

    def check_result(self, case, actual, msg):
        self.assertCountEqual(case.expected, actual, msg=msg)


if __name__ == '__main__':
    unittest.main()
