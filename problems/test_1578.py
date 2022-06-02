import unittest
from typing import List

import utils


# O(n) time. O(1) space. Greedy.
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        prev_char = colors[0]
        prev_cost = neededTime[0]

        for i in range(1, len(colors)):
            curr_char = colors[i]
            curr_cost = neededTime[i]

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
