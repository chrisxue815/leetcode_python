import unittest
from typing import List

import utils
from tree import TreeNode


def _find_predecessor(curr):
    p = curr.left
    if not p:
        return None
    while p.right and p.right is not curr:
        p = p.right
    return p


# O(n) time. O(1) space. Morris in-order traversal.
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        curr = root

        while curr:
            p = _find_predecessor(curr)

            if p:
                if p.right:
                    result.append(curr.val)
                    p.right = None
                    curr = curr.right
                else:
                    p.right = curr
                    curr = curr.left
            else:
                result.append(curr.val)
                curr = curr.right

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().inorderTraversal(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
