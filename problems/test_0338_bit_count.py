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
    def countBits(self, n: int) -> List[int]:
        return [bit_count(x) for x in range(n + 1)]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
