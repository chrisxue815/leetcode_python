import unittest

import utils


# O(nlog(n)) time. O(n) space. Greedy, intuition, deductive reasoning, sort.
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs = sorted(((a - b, a, b) for a, b in costs))

        sum_a = sum(a for _, a, _ in costs[:len(costs) // 2])
        sum_b = sum(b for _, _, b in costs[len(costs) // 2:])

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
