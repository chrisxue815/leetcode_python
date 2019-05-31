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


def _reverse_append(result, start):
    curr = start
    prev = None
    while curr:
        curr.right, prev, curr = prev, curr, curr.right

    curr = prev
    prev = None
    while curr:
        result.append(curr.val)
        curr.right, prev, curr = prev, curr, curr.right


# O(n) time. O(1) space. Morris post-order traversal.
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        dummy = TreeNode(0)
        dummy.left = root
        curr = dummy

        while curr:
            p = _find_predecessor(curr)

            if p:
                if p.right:
                    p.right = None
                    _reverse_append(result, curr.left)
                    curr = curr.right
                else:
                    p.right = curr
                    curr = curr.left
            else:
                curr = curr.right

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().postorderTraversal(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
