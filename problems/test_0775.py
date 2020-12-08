import unittest
from typing import List

import utils


# O(n) time. O(1) space. Math, array.
# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all(abs(i - num) <= 1 for i, num in enumerate(A))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().isIdealPermutation(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
