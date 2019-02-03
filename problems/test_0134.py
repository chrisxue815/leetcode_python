import unittest


# O(n). Mathematical modelling and reasoning
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
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
        self._test([1, 2, 3, 3], [2, 1, 5, 1], 3)

    def _test(self, gas, cost, expected):
        actual = Solution().canCompleteCircuit(gas, cost)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
