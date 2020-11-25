import unittest
from typing import List

import utils


# O(n) time. O(n) space. Hash table, hash set, recording pairs.
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        visited = set()
        pairs = set()

        for num in nums:
            if num - k in visited:
                pairs.add((num - k, num))
            if num + k in visited:
                pairs.add((num, num + k))
            visited.add(num)

        return len(pairs)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findPairs(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
