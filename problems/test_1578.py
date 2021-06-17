import unittest
from typing import List

import utils


# O(n) time. O(1) space. Greedy.
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        result = 0
        prev_char = s[0]
        prev_cost = cost[0]

        for i in range(1, len(s)):
            curr_char = s[i]
            curr_cost = cost[i]

            if curr_char != prev_char:
                prev_char = curr_char
                prev_cost = curr_cost
            elif curr_cost > prev_cost:
                result += prev_cost
                prev_cost = curr_cost
            else:
                result += curr_cost

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
