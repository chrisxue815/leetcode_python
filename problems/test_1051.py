import unittest

import utils


# O(n) time. O(n) space. Counting sort.
class Solution:
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        result = 0
        counts = [0] * 101

        for h in heights:
            counts[h] += 1

        i = 0
        for h in range(1, 101):
            bound = i + counts[h]

            while i < bound:
                if heights[i] != h:
                    result += 1
                i += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().heightChecker(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
