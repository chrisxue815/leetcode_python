import collections
import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Counting sort, hash table, sort.
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        counts = collections.Counter(arr1)

        for num in arr2:
            result += [num] * counts[num]
            del counts[num]

        for num, count in sorted(counts.items()):
            result += [num] * count

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().relativeSortArray(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
