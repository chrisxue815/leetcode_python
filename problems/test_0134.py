import unittest
from typing import List

import utils


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = total = curr = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            curr += diff
            if curr < 0:
                start = i + 1
                curr = 0

        return start if total >= 0 else -1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
