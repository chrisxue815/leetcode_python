import collections
import unittest
from typing import List

import utils


# O(n) time. O(n) space. Counting, combination.
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = collections.Counter((a, b) if a <= b else (b, a) for a, b in dominoes)
        return sum(count * (count - 1) // 2 for count in counts.values())


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().numEquivDominoPairs(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
