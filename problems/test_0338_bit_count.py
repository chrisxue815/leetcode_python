import unittest
from typing import List

import utils


def bit_count(x):
    # Hacker's Delight, Figure 5-2
    # See OpenJDK Integer.bitCount():
    # https://github.com/openjdk/jdk/blob/f37d9c8abca50b65ed232831a06d60c1d015013f/src/java.base/share/classes/java/lang/Integer.java#L1685
    x = x - ((x >> 1) & 0x55555555)  # (xx & 01) + ((xx >> 1) & 01) == xx - ((xx >> 1) & 01)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f
    x += x >> 8
    x += x >> 16
    return x & 0x3f


# O(n * log(sizeof(integer))) time. O(1) space. Bit count.
class Solution:
    def countBits(self, num: int) -> List[int]:
        return [bit_count(x) for x in range(num + 1)]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().countBits(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
