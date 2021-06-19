import unittest

import utils


# O(n) time. O(1) space. Greedy.
class Solution:
    def minOperations(self, s: str) -> int:
        starts_with_0 = 0
        starts_with_1 = 0

        for i, c in enumerate(s):
            if (i & 1 == 0) == (c == '0'):
                starts_with_1 += 1
            else:
                starts_with_0 += 1

        return min(starts_with_0, starts_with_1)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
