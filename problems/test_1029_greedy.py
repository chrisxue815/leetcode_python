import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Greedy, intuition, deductive reasoning, sort.
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[0] - cost[1])

        sum_a = sum(a for a, _ in costs[:len(costs) // 2])
        sum_b = sum(b for _, b in costs[len(costs) // 2:])

        return sum_a + sum_b


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().twoCitySchedCost(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
