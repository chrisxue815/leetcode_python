import unittest
import utils


# O(n) time. O(n) space. Stack.
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev_i = stack.pop()
                result[prev_i] = i - prev_i

            stack.append(i)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p739.json').test_cases

        for case in cases:
            actual = Solution().dailyTemperatures(case.temperatures)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
