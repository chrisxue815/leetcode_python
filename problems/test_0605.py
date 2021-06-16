import unittest
from typing import List

import utils


# O(n) time. O(1) space. Array.
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n <= 0:
            return True

        prev = -2
        for i, planted in enumerate(flowerbed):
            if planted:
                n -= (i - prev - 2) >> 1
                if n <= 0:
                    return True
                prev = i

        n -= (len(flowerbed) - prev - 1) >> 1
        return n <= 0


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
