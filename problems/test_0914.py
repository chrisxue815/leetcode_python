import collections
import math
import unittest
from typing import List

import utils


# O(n) time. O(n) space. Math, GCD, hash table.
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = collections.Counter(deck)
        gcd = next(iter(counts.values()))

        for count in counts.values():
            gcd = math.gcd(gcd, count)
            if gcd == 1:
                return False

        return True


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().hasGroupsSizeX(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
