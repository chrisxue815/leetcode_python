import unittest
from typing import List

import utils


# O(n) time. O(1) space. Stack.
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0

        for x in pushed:
            pushed[i] = x

            while i >= 0 and pushed[i] == popped[j]:
                i -= 1
                j += 1

            i += 1

        return j == len(popped)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().validateStackSequences(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
