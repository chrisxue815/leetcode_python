import unittest

import utils


# O(n) time. O(1) space. Counting leaves.
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        leaves = 1
        i = 0

        while i < len(preorder):
            if preorder[i] == '#':
                leaves -= 1
                i += 2
                if leaves == 0 and i < len(preorder):
                    return False
            else:
                leaves += 1
                i += 1
                while i < len(preorder) and preorder[i] != ',':
                    i += 1
                i += 1

        return leaves == 0


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().isValidSerialization(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
