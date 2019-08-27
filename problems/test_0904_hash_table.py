import collections
import unittest
from typing import List

import utils


# O(n) time. O(1) space. Sliding window, hash table.
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        result = 0
        counter = collections.Counter()
        lo = 0
        hi = 0

        while True:
            # Expand
            while hi < len(tree) and (len(counter) < 2 or tree[hi] in counter):
                counter[tree[hi]] += 1
                hi += 1

            result = max(result, sum(counter.values()))

            if hi >= len(tree):
                break

            # Shrink
            while len(counter) >= 2:
                counter[tree[lo]] -= 1
                if counter[tree[lo]] <= 0:
                    del counter[tree[lo]]
                lo += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().totalFruit(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
