import collections
import unittest
from typing import List

import utils


# O(n) time. O(n) space. Hash table, counting.
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0 or not nums:
            return 0

        counter = collections.Counter()

        for num in nums:
            counter[num] += 1

        num_pairs = 0
        if k == 0:
            for num, count in list(counter.items()):
                if count >= 2:
                    num_pairs += 1
        else:
            for num in counter:
                if counter[num + k] > 0:
                    num_pairs += 1

        return num_pairs


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findPairs(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
